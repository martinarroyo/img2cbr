#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Creates a .cbr file from a list of image files
"""

from __future__ import absolute_import
import argparse
import os
import sys
from librar import archive
import re
import six
parser = argparse.ArgumentParser(description="Creates a .cbr file from a list of image files")

parser.add_argument('folder',
                    type=str,
                    help="the name of the directory")
parser.add_argument('-f',
                    '--formats',
                    type=list,
                    help="The filetypes to process. png, jpg, jpeg by default",
                    metavar="format",
                    nargs="*",
                    default=["png", "jpg", "jpeg"])
parser.add_argument('-o', '--output', type=str, help="The output filename", metavar="output", default="")
parser.add_argument('-v', '--verbose', dest="verbose", action="store_true")
res = parser.parse_args()

if not os.path.isdir(res.folder):
    sys.stderr.write("The directory does not exist! Exiting")
    sys.exit(1)

def file_types(path, *extensions):
    """
    Returns all files in the path that match the filetypes
    """
    for file_name in os.listdir(path):
        if re.match(r".*\." + "|".join(extensions), file_name):
            yield os.path.join(path, file_name)

if res.output:
    filename = ref.output
else:
    directory = os.path.basename(os.path.normpath(res.folder))
    filename = directory + ".cbr"
if six.PY2:
    basedir = os.getcwdu()
else:
    basedir = os.getcwd()
rarfile = archive.Archive(filename, basedir)
#rarfile.use_syslog()

for filename in file_types(res.folder, *res.formats):
    rarfile.add_file(filename)

rarfile.set_compression_level(0)
rarfile.set_recovery_record(5)
rarfile.run(silent=not res.verbose)

