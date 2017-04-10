#Task runner
import sys
import SortHelper
import Misc

print("Enter M")
M = int(input())
print(M)
print("Enter Profit list")
plist = list(map(int, input().strip().split(' ')))
print("Profit list", plist)

print("Enter City list")
clist = list(map(int, input().strip().split(' ')))
print("City list", clist)

print("Enter Visit list")
vlist = list(map(int, input().strip().split(' ')))
print("Visit list", vlist)

profit = Misc.getMaxProfit(M, plist, clist, vlist)
print("Max profit is ", profit)
#print(ulist)
#SortHelper.BubbleSort(ulist)
#SortHelper.SelectionSort(ulist)
#SortHelper.QuickSort(ulist)
#print(ulist)
