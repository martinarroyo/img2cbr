img2cbr
=======

A simple utility to create a cbr file from a list of image files.

The script depends on miebach's [lib-rar-python](https://github.com/miebach/lib-rar-python). There's a [pull request](https://github.com/miebach/lib-rar-python/pull/3) that adds Python 3 compatibility. However, it is not yet accepted. If you want to use Python 3, there is a [fork](https://github.com/Alternhuman/lib-rar-python) you can use.

Usage
-----

> usage: img2cbr.py [-h] [-f format [format ...]] [-o output] folder

Creates a .cbr file from a list of image files

positional arguments:
  folder                the name of the directory

optional arguments:
  -h, --help            show this help message and exit
  -f format [format ...], --formats format [format ...]
                        The filetypes to process. png, jpg, jpeg by default
  -o output, --output output
                        The output filename
