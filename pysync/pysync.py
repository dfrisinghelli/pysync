import os
import sys
import shutil
from datetime import datetime

class PySync:
    
    # initialise class with instance attributes
    # source and target
    def __init__(self, source, target):
        self.source = os.path.normpath(source)
        self.target = os.path.normpath(target)
        
        # check if source directory exists
        if not os.path.isdir(self.source):
            print('Source directory {} does not exist'.format(self.source))
            sys.exit()

        # create target directory if it does
        # not yet exist
        if not os.path.isdir(self.target):
            print('Creating target directory {}'.format(self.target))
            os.makedirs(self.target)
    
    # creates correct path in the target directory
    def _dpath(self, dirpath, dirname):
        return os.path.join(self.target,
                            os.path.relpath(dirpath, self.source),
                            dirname)

    # compares modified time of files in the 
    # source and target directories, returns
    # True if file was modified               
    def _ifmod(self, source, target):

        # get modification times of source and target files
        mtime_s = os.path.getmtime(source)
        mtime_t = os.path.getmtime(target)

        return datetime.fromtimestamp(mtime_s) > datetime.fromtimestamp(mtime_t)
    
    # deletes files that were removed from the source directory
    def _del(self, path):

        # recursively delete everything in path
        # if path is a directory
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            # delete path if path is a file
            os.unlink(path)


    def sync_dir(self, dirpath, dirnames):

        # loop through the subdirectories in 
        # the current directory path
        for dir in dirnames:
            dpath = self._dpath(dirpath, dir)

            # check if the current directory already
            # exists in the target
            if not os.path.exists(dpath):
                print('mkdir {}'.format(dpath))
                os.mkdir(dpath)
    
    def sync_files(self, dirpath, filenames):

        # loop through the files in the current
        # directory path
        for file in filenames:
            sfile = os.path.join(dirpath, file)
            dfile = self._dpath(dirpath, file)

            # check if file already exists and if
            # yes, check if it was modified in the
            # source directory
            if os.path.isfile(dfile):
                if not self._ifmod(sfile, dfile):
                    continue
            
            print("copy {}".format(dfile))
            shutil.copy2(sfile, dfile)
    
    def sync_deleted(self, dirpath, dirnames, filenames):
        
        # directories and files in the current dirpath
        # in the source directory
        sdirs = set(dirnames)
        sfiles = set(filenames)

        # get the directories and files in the current dirpath
        # in the target directory
        _, tdirs, tfiles  = next(os.walk(self._dpath(dirpath, "")))

        # check if there are directories in the target directory
        # that have been removed in the source directory
        diff_dir = set(tdirs) - sdirs

        # check if there are files in the target directory
        # that have been removed in the source directory
        diff_files = set(tfiles) - sfiles

        for to_remove in diff_dir.union(diff_files):
            # get correct path in the target directory
            to_remove = self._dpath(dirpath, to_remove)
            print("del {}".format(to_remove))

            # remove directory/file in the target directory
            self._del(to_remove)

    def sync(self):

        # "walk" through the source directory and copy
        # subdirectories and files to the target directory
        for dirpath, dirnames, files in os.walk(self.source):
            
            # synchronize directories
            self.sync_dir(dirpath, dirnames)

            # synchronize files
            self.sync_files(dirpath, files)

            # check if files were removed in the source directory
            self.sync_deleted(dirpath, dirnames, files) 
        