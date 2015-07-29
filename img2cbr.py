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
from six.moves import getcwdu

parser = argparse.ArgumentParser(description="Creates a .cbr file from a list of image files")

parser.add_argument('folder',
                    type=str,
                    help="the name of the directory")
parser.add_argument('-f',
                    '--formats',
                    type=str,
                    help="The filetypes to process. png, jpg, jpeg by default",
                    metavar="format",
                    nargs="+",
                    default=["png, jpg, jpeg"])
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


directory = os.path.basename(os.path.normpath(res.folder))
filename = directory + ".cbr"

rarfile = archive.Archive(filename, getcwdu)
rarfile.use_syslog()
for filename in file_types(res.folder, *res.formats):
    rarfile.add_file(filename)

rarfile.set_compression_level(0)
rarfile.set_recovery_record(5)
rarfile.run(silent=False)

