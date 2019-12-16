#!/usr/bin/env python3

import os
import glob
import sys
import argparse

parser = argparse.ArgumentParser(usage='mren filetype newname [-h] [-v] [-n <int>]', description='rename all files of chosen type in a directory')
parser.add_argument('filetype', type=str, help='choose filetype for all the files you want to rename')
parser.add_argument('newname', type=str, help='choose new name for all files chosen')
parser.add_argument('-v', '--verbose', action='store_true', help='make output verbose')
parser.add_argument('-V', '--version', action='version', version='mren 1.0', help='show program\'s version number and exit')
parser.add_argument('-n', '--number', type=int, metavar='<int>', help='set number of placeholder digits in filenumber. default is 4, maximum is 10')
parser.add_argument('-d','--directory', type=str, metavar='<directory>', help='specify a directory. Default is current working directory')
args = parser.parse_args()

ftype = args.filetype

if args.filetype[0] == '.':
    args.filetype = args.filetype[1:]

os.chdir(os.getcwd())
if args.directory is not None:
    os.chdir(args.directory)

files = []

count = 0

if args.verbose: 
    print('\n-mren version 1.0-\n')

digitVal = args.number
if args.number is None:
    digitVal = 4
elif args.number > 10:
    parser.error('-n must be 10 or less. Come on.')
elif args.number < 1:
    parser.error('-n must be greater than 0.')

for file in glob.glob('*.' + args.filetype):
    files.append(file)

for i in files:
   count += 1
   filenum = str(count).zfill(digitVal)
   os.rename(i, args.newname + str(filenum) + '.' + args.filetype)
   if args.verbose:
       print(f"Renaming {i} to {args.newname + str(filenum)}.{args.filetype}...")
print('\nDone')
