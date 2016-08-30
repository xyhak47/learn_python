# Author: xyh
# Date: 2016.8.26
# File line counter

import sys, os

filePathDir = []
totalLines = 0
targetPath = ''
copyFilePath = ''

def handle_all_files(_copyFilePath):
    if _copyFilePath == '':
        print 'copyFilePath is empty'
        return

    global totalLines

    copyFile = open(_copyFilePath, 'r+')

    for path in filePathDir:
        file = open(path,'r')

        fileContent = file.read()
        copyFile.write(fileContent)

        # fileContent = fileContent.split('\n')
        # totalLines += len(fileContent)
        # print fileContent
        file.close()

        totalLines += sum(1 for line in open(path))

   # print copyFile.read()
    print 'copy file succeed!'
    copyFile.close()


def deep_iterate_dir(_targetPath):
    if _targetPath == '':
        return

    for _list in os.listdir(_targetPath):
        path = os.path.join(_targetPath, _list)
        if os.path.isdir(path):
            deep_iterate_dir(path)
        elif os.path.isfile(path):
            if isCsFile(path):
                filePathDir.append(path)
                print path + '\n'
            else:
                print path + '  ==> ignored' + '\n'


def isCsFile(path):
    return os.path.splitext(path)[1] == '.cs'


def main(argv): 
    global targetPath
    global copyFilePath

    targetPath = argv[0]
    copyFilePath = argv[1]
    print 'targetPath = ' + targetPath     
    print 'copyFilePath = ' + copyFilePath     

    print '******************** all cs file path begin **************************'
    deep_iterate_dir(targetPath) 
    print '******************** all cs file path end **************************'
  
    handle_all_files(copyFilePath) 
    print 'totalLines = ' +  str(totalLines)


if __name__ == "__main__":
    main(sys.argv[1:])
