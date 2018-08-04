from timeit import Timer

def printStatistics(type,outerCount,innerCount,swapCount):
    print("{0:20}{1:16}{2:18}{3:16}".format(type,outerCount,innerCount,swapCount))
    
def bubbleSort(alist):

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
                temp = alist[innerIndex]
                alist[innerIndex] = alist[innerIndex+1]
                alist[innerIndex+1] = temp
                #print(alist)
    return outerCount,innerCount,swapCount

def selectionSort(alist):
    listLen = len(alist)
    outerCount = 0
    innerCount = 0
    swapCount = 0
    for outerIndex in range(listLen):
        outerCount += 1
        for innerIndex in range(outerIndex+1, listLen):
            innerCount += 1
            
            if alist[innerIndex] < alist[outerIndex]:
                swapCount += 1
                temp = alist[outerIndex]
                alist[outerIndex] = alist[innerIndex]
                alist[innerIndex] = temp
                #print(alist)
    return outerCount,innerCount,swapCount

def insertionSort(alist):
    outerCount = 0
    innerCount = 0
    swapCount = 0
    for index in range(1,len(alist)):
        outerCount += 1
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            innerCount += 1
            alist[position]=alist[position-1]
            position = position-1
            swapCount += 1
            
        alist[position]=currentvalue
    return outerCount,innerCount,swapCount


sortedList = [1,2,3,4,5,6,7,8,9,10]
longSortedList = list(range(1000))
#bUnsortedList = [10,9,8,7,6,5,4,3,2,1]
bUnsortedList = [7,4,6,9,10,2,1,3,5,8]
sUnsortedList = [7,4,6,9,10,2,1,3,5,8]
iUnsortedList = [7,4,6,9,10,2,1,3,5,8]

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


t1 = Timer("bubbleSort(longSortedList)", "from __main__ import bubbleSort, longSortedList")
print("BubbleSort with large sorted list    ",t1.timeit(number=100), "seconds")

t2 = Timer("selectionSort(longSortedList)", "from __main__ import selectionSort, longSortedList")
print("SelectionSort with large sorted list ",t2.timeit(number=100), "seconds")

t3 = Timer("insertionSort(longSortedList)", "from __main__ import insertionSort, longSortedList")
print("InsertionSort with large sorted list ",t3.timeit(number=100), "seconds")


