import os
import glob
import sys
import argparse

parser = argparse.ArgumentParser(description='Rename all files of chosen type in a directory.')
parser.add_argument('filetype', type=str, help='Choose filetype for all the files you want to rename.')
parser.add_argument('newname', type=str, help='Choose new name for all files chosen.')

parser.add_argument('-v', '--verbose', action='store_true', help='Make output verbose.')
args = parser.parse_args()

ftype = args.filetype

if args.filetype[0] == '.':
    args.filetype = args.filetype[1:]

os.chdir(os.getcwd())

files = []

count = 0

for file in glob.glob('*.' + args.filetype):
    files.append(file)

for i in files:
   count += 1
   filenum = '{:0>4}'.format(count)
   os.rename(i, args.newname + str(filenum) + '.' + args.filetype)
   if args.verbose:
       print(f"Renaming {i} to {args.newname + str(filenum)}.{args.filetype}")
print('Done')

