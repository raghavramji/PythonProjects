def bubbleSort(l):
  for i in range(len(l)):
    k = l[i]
    kI = i
    for j in range(i, len(l)):
        if l[j] < k:
          k = l[j]
          kI = j
    t = l[i]
    l[i] = k
    l[kI] = t
  return l
print(bubbleSort([1,7,5,3]))
      
      
      
      
      
''' t = lst[i]
    lst[i] = maxItem
    lst[maxItemI] = t'''
