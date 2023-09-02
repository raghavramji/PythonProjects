# main.py
def merge(l1,l2): # merges two sorted lists
  merged_list = []
  while len(l1) > 0 and len(l2) > 0:
    if l1[0] < l2[0]:
      merged_list.append(l1.pop(0))
    else:
      merged_list.append(l2.pop(0))
  return merged_list + l1 + l2 


#print(merge([3,6,8,9,78],[5,7,8,17,56,137]))




def merge_sort(input_l): # splits a list into two lists to sort it
  n = len(input_l)
  if n <= 1:
    return input_l
  print(input_l)
  #split into two sublists
  firstHalf = merge_sort(input_l[:n//2])
  secondHalf = merge_sort(input_l[n//2:])
  return merge(firstHalf,secondHalf) #once the lists are sorted, merge them
  
print(merge_sort([10,8,23,405,87,45]))
