#!/usr/bin/env python3
# coding: utf-8

# Flatten and unflatten directories
#
# Usage:
#   $ python3 dirflatter.py [options] <targetdir>
#
# Options:
#   --unflatten                unflatten directory structure
#   --separater <SEPARATER>    change separater

from pathlib import Path, PurePath


def flatter(args):
    """flatten directory structure"""
    targetdir = Path(args.targetdir)
    separater = args.separater
    print('flatten:', targetdir)
    print('separater:', separater)
    print('----')

    delete_dict = {}
    for p in targetdir.glob('*/*'):
        if p.is_file():
            subdir = p.parent.name
            filename = p.name
            delete_dict[p.parent.name] = p.parent
            # flatten
            newfilename = targetdir / (subdir + separater + filename)
            p.rename(newfilename)
            print('rename:', p, '->', newfilename)

    # delete empty subdir
    for unneeded in delete_dict.values():
        try:
            unneeded.rmdir()
        except OSError as e:
            if e.errno == 66:
                pass
                print('Directory not empty:', unneeded)


def unflatter(args):
    """unflatten directory structure"""
    targetdir = Path(args.targetdir)
    separater = args.separater
    print('unflatten:', targetdir)
    print('separater:', separater)
    print('----')

    for p in targetdir.iterdir():
        if p.is_file():
            splitted_path = p.name.split(separater,1)
            if len(splitted_path) == 2:
                subdir = Path(splitted_path[0])
                filename = Path(splitted_path[1])
                # create sub-directory
                subdir = targetdir / subdir
                subdir.mkdir(exist_ok=True)
                newfilename = subdir / filename
                p.rename(newfilename)
                print('rename:', p, '->', newfilename)


if __name__ == "__main__":
    import argparse
    # parse args
    parser = argparse.ArgumentParser(description="Flatten and unflatten directories",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('targetdir', action='store', type=str,
                        help='directory you want to flatten or unflatten')
    parser.add_argument('--unflatten', action='store_true', default=False,
                        help='unflatten directory structure')
    parser.add_argument('--separater', type=str, default="_-_",
                        help='change separater')
    args = parser.parse_args()

    if args.unflatten:
        unflatter(args)
    else:
        flatter(args)
