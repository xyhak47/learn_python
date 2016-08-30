# Author: xyh
# Date: 2016.8.26
# File line counter

import sys, os

totalLines = 0
filePathDir = []

def handle_all_files():
    global totalLines
    for filePath in filePathDir:
        totalLines += sum(1 for line in open(filePath))


def deep_iterate_dir(rootDir):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        if os.path.isdir(path):
            deep_iterate_dir(path)
        elif os.path.isfile(path):
            if isCsFile(path):
                filePathDir.append(path)
                print path + '\n'


def isCsFile(path):
    return os.path.splitext(path)[1] == '.cs'


def main(argv):  
    targetPath = argv[0]
    print 'targetPath = ' + targetPath     

    print '******************** all cs file path begin **************************'
    deep_iterate_dir(targetPath) 
    print '******************** all cs file path end **************************'
  
    handle_all_files() 
    print 'totalLines = ' +  str(totalLines)


if __name__ == "__main__":
    main(sys.argv[1:])
