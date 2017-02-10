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

