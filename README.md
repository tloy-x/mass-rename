# Mass Renamer
Simple python mass-renamer

```
usage: mren.py filetpe newname [-h] [-v] [-n <int>] [-d <directory>]

rename all files of chosen type in a directory.

positional arguments:
  filetype              choose filetype for all the files you want to rename.
  newname               choose new name for all files chosen.

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         make output verbose.
  -n <int>, --number <int>
                        set number of placeholder digits in filenumber.
                        default is 4. maximum is 10.
  -d <directory>, --directory <directory>
                        Specify a directory. Default is current working
                        directory.
```
