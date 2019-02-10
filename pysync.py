import os
import sys

class pybackup:
    
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
    
    def _dpath(self, dirpath, dirname):
        return os.path.join(self.target, os.path.relpath(dirpath, self.source), dirname)

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
    
    def sync(self):

        for dirpath, dirnames, files in os.walk(self.source):

            self.sync_dir(dirpath, dirnames)



        
        
        
        
        
    