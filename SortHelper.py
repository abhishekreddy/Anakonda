import sys

def BubbleSort(ulist):
    """This function will sort the given list using bubble sort"""
    done = 0 #This variable is used to break the loop when sorting is done
    while not done:
        done = 1
        for i in range(len(ulist) - 1):
            if ulist[i] > ulist[i+1]:
                ulist[i], ulist[i+1] = ulist[i+1], ulist[i]
                done = 0



def SelectionSort(ulist):
    """This function will sort the given list using selection sort"""
    for i in range(len(ulist)):
        mini = ulist[i]
        mpos = i;
        for j in range(i, len(ulist)):
            if mini < ulist[j]:
                mini = ulist[j]
                mpos = j
        ulist[i], ulist[mpos] = ulist[mpos], ulist[j]

def __Partition(ulist, start, stop):
    """A priavte function to help in quick sort"""
    i = start - 1
    pivot = ulist[stop]
    for j in range(start, stop):
        if ulist[j] <= pivot:
            i += 1
            ulist[i], ulist[j] = ulist[j], ulist[i]
    ulist[i+1],ulist[stop] = ulist[stop], ulist[i+1]
    return i+1

def __QuickSortHelper(ulist, start, stop):
    """A private function to help in quick sort"""
    if start < stop:
        i = __Partition(ulist, start, stop)
        __QuickSortHelper(ulist, start, i -1)
        __QuickSortHelper(ulist, i+1, stop)

def QuickSort(ulist):
    """This functon will sort the given list using quick sort"""
    __QuickSortHelper(ulist, 0, len(ulist)-1)



        
