#!/usr/bin/env python
import sys

def error(str):
    sys.stderr.write(str)
    sys.stderr.flush()
    
    
def readLinesFromFile(fileName):
    lines = []
    with open(fileName) as fp:
        for line in fp:
            lines.append(line)
    return lines

def magicIsRight(magic):
    return magic == 'LINK\n'

def getNumbers(numberline,numbers):
    nums = numberline.split(' ')
    nums = filter(lambda x:x !=' ',nums)
    numbers['nsegs'] = int(nums[0])
    numbers['nsyms'] = int(nums[1])
    numbers['nrels'] = int(nums[2])
    return numbers

def getSegments(fileList,numbers,List):
    for i in range(numbers['nsegs']):
        segmentTextList = fileList[i+2].split(' ')
        segmentTextList = filter(lambda x:x !=' ',segmentTextList)
        
        segment = {}
        segment['name'] = segmentTextList[0]
        segment['entry'] = int(segmentTextList[1])
        segment['length'] = int(segmentTextList[2])
        segment['flags'] = filter(lambda x:x!='\n',segmentTextList[3])
        segItem = []
        segItem.append(segment)
        List.append(segItem) 
    return List 

def getSymbols(fileList,number,List):
    offset = numbers['nsegs']+2
    for i in range(numbers['nsyms']):
        
        symbolTextList = fileList[i+offset].split(' ')
        symbolTextList = filter(lambda x:x !=' ',symbolTextList)
        print symbolTextList
        symbol = {}
        symbol['name'] = symbolTextList[0]
        symbol['value'] = symbolTextList[1]
        symbol['type'] = filter(lambda x:x!='\n',symbolTextList[3])
        seg = int(symbolTextList[2])
        List[seg].append(symbol)
    return List

if __name__ == '__main__':
    argvs = len(sys.argv)
    if argvs != 2 :
        error("Error:unsafe arguments")
        
    bigList = []
    bigList.append([{'name':'null'}])
    
    filename = sys.argv[1]
    fileList = readLinesFromFile(filename)
    
    if magicIsRight(fileList[0]):
        numbers = {}
        numbers = getNumbers(fileList[1],numbers)
        bigList = getSegments(fileList,numbers,bigList)
        bigList = getSymbols(fileList,numbers,bigList)
        print bigList
    
    

        
    
    
    
    




