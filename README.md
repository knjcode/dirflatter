# dirflatter

Flatten and unflatten directories.

## Example directory strucure

```
images
├── airplanes
│   ├── airplane001.jpg
│   └── airplane002.jpg
└── watch
    ├── watch001.jpg
    └── watch002.jpg
```

## Flatten contents of sub-directories down to one directory

```
$ python3 dirflatter.py images
$ tree images
images
├── airplanes_-_airplane001.jpg
├── airplanes_-_airplane002.jpg
├── watch_-_watch001.jpg
└── watch_-_watch002.jpg

0 directories, 4 files
```

## Unflatten directory structure

```
$ python3 dirflatter.py --unflatten images
$ tree images
images
├── airplanes
│   ├── airplane001.jpg
│   └── airplane002.jpg
└── watch
    ├── watch001.jpg
    └── watch002.jpg

2 directories, 4 files
```

## Change separater

By default, `_-_` is used to separate directory names and file names.

You can change this value with the `--separater` option.
