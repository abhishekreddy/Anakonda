#Task runner
import sys
import SortHelper

ulist = list(map(int, input().strip().split(' ')))

print(ulist)
#SortHelper.BubbleSort(ulist)
SortHelper.SelectionSort(ulist)
print(ulist)
