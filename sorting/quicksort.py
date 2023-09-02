# main.py
import random
input_l = []
for i in range(10):
  n = random.randint(1,10)
  input_l.append(n)


def Partition(lst, pivot):
  less = []   # Alternatively explain how to do multiple assignments, like so:
  eq = []     # less, eq, great = [[] for i in range(3)]
  great = []

  for num in lst:
    if num < pivot:
      less.append(num)
    elif num == pivot:
      eq.append(num)
    else:
      great.append(num)

  return less, eq, great
#Partition(input_l, 0)


def quicksort(lst):
  n = len(lst)
  if n <= 1:
    return lst
  pivotInd = lst[0]
  less,eq,great = Partition(input_l, pivotInd)
  sortedless = quicksort(less)
  sortedgreater = quicksort(great)
  return sortedless+eq+sortedgreater
  
print(quicksort(input_l))
