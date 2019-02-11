# pysync

`pysync` is a small `Python` package that allows backing up data between two
directories. The majority of the code follows the example 
[here](https://codereview.stackexchange.com/questions/143949/building-an-efficient-python-backup-module).

## Requirements
It requires `Python 3` or greater and it's dependencies can be found in the `setup.py` file.

## Installation
Download `pysync` [here](https://github.com/dfrisinghelli/pysync)
or alternatively use `git` from terminal:

```bash,
git clone https://github.com/dfrisinghelli/pysync
```

This creates a copy of the repository in your current directory on the file
system. To install `pysync`, open a terminal and **in the projects root directory**
type:

```bash,
pip install -e .
```
The package is now accessible from everywhere in your file system.

## Import
Once installed, you can import the package in a python environment using

```python,
import pysync
```
Since the actual class `PySync` is in the `pysync.py` module use:

```python,
from pysync.pysync import PySync
```

## Instantiation
Once imported, in your Python environment type,

```python,
mybackup = PySync('source', 'target')
```
replacing `source` by the **path to the directory you want to backup** and `target` by the **path to the directory you want to store the backup** of `source` to. Then use the method `sync` to start the backup process:

```python,
mybackup.sync()
```

This will backup all directories, subdirectories and files in `source` to `target`. If you remove or modify files in `source`, just rerun

```python,
mybackup.sync()
```
and the changes will also be made in `target`.

## Command line
Alternatively, you can use the `pysync` command line tool. Once the package is installed, from a terminal you can type,

```bash,
pysync <source> <target>
```
again replacing `<source>` and `<target>` by the respective directories.
