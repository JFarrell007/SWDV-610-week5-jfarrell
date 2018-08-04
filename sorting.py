"""
Name: Jim Farrell
Description: show how list is is sorted with bubble sort, selection sort and insertion sort
"""
from timeit import Timer

#large sorted list for timing
longSortedList = list(range(1000))

def printStatistics(type,outerCount,innerCount,swapCount):
    """Prints statistics for loop counts and swap count"""
    print("{0:20}{1:16}{2:18}{3:16}".format(type,outerCount,innerCount,swapCount))
    
def bubbleSort(alist):
    """bubbleSort funciton"""

    outerCount = 0
    innerCount = 0
    swapCount = 0
    lenList = len(alist) - 1
    for outerIndex in range(lenList):
        outerCount += 1
        for innerIndex in range(lenList):
            innerCount += 1
            if alist[innerIndex]>alist[innerIndex+1]:
                swapCount += 1
                alist[innerIndex],alist[innerIndex+1] = alist[innerIndex+1], alist[innerIndex]
        #print(alist)
    return outerCount,innerCount,swapCount

def selectionSort(alist):
    """selectionSort function"""
    listLen = len(alist)
    outerCount = 0
    innerCount = 0
    swapCount = 0
    for outerIndex in range(listLen -1, 0, -1):
        outerCount += 1
        positionOfMax = 0
        for innerIndex in range(1, outerIndex+1):
            innerCount += 1
            if alist[innerIndex] > alist[positionOfMax]:
                positionOfMax = innerIndex
            alist[outerIndex],alist[positionOfMax] = alist[positionOfMax],alist[outerIndex]
            swapCount += 1
        #print(alist)
    return outerCount,innerCount,swapCount
                


def insertionSort(alist):
    """insertionSort function"""
    outerCount = 0
    innerCount = 0
    swapCount = 0
    listLen = len(alist)
    for index in range(1,listLen):
        outerCount += 1
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            innerCount += 1
            alist[position]=alist[position-1]
            position = position-1
            swapCount += 1
                
        alist[position]=currentvalue
        #print(alist)
        
    return outerCount,innerCount,swapCount


def testIt():
    """function to run tests with sorting algorithms"""
    #sortedList used by all sorting functions
    sortedList = [1,2,3,4,5,6,7,8,9,10]
    #Need to use three unsorted lists since the list will be sorted after first used
    bUnsortedList = [10,9,8,7,6,5,4,3,2,1]
    sUnsortedList = [10,9,8,7,6,5,4,3,2,1]
    iUnsortedList = [10,9,8,7,6,5,4,3,2,1]

    print("....................Outer Iterations  Inner Iterations  Number of Swaps")

    outerCount,innerCount,swapCount = bubbleSort(sortedList)
    printStatistics("Sorted Bubble",outerCount,innerCount,swapCount)
    outerCount,innerCount,swapCount = bubbleSort(bUnsortedList)
    printStatistics("Unsorted Bubble",outerCount,innerCount,swapCount)

    outerCount,innerCount,swapCount = selectionSort(sortedList)
    printStatistics("Sorted Selection",outerCount,innerCount,swapCount)
    outerCount,innerCount,swapCount = selectionSort(sUnsortedList)
    printStatistics("Unsorted Selection",outerCount,innerCount,swapCount)

    outerCount,innerCount,swapCount = insertionSort(sortedList)
    printStatistics("Sorted Insertion",outerCount,innerCount,swapCount)
    outerCount,innerCount,swapCount = insertionSort(iUnsortedList)
    printStatistics("Unsorted Insertion",outerCount,innerCount,swapCount)


    #Set up timers to time the various sorting algorithms with large lists multiple or number= times
    t1 = Timer("bubbleSort(longSortedList)", "from __main__ import bubbleSort, longSortedList")
    print("BubbleSort with large sorted list    ",t1.timeit(number=50), "seconds")

    t2 = Timer("selectionSort(longSortedList)", "from __main__ import selectionSort, longSortedList")
    print("SelectionSort with large sorted list ",t2.timeit(number=50), "seconds")

    t3 = Timer("insertionSort(longSortedList)", "from __main__ import insertionSort, longSortedList")
    print("InsertionSort with large sorted list ",t3.timeit(number=50), "seconds")
    
testIt()


