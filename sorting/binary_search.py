def binary(l,n):
 
  if len(l) == 0:
    return False
  
  m = int(len(l) / 2) 
   
  if l[m] == n:
     return True
  elif len(l) == 1:
     return False
     
  if n > l[m]:
    return binary(l[m:],n)
  elif n < l[m]:
    return binary(l[:m],n)
  
  return False
  
mylist = [1,2,3,4,5,6,7]
    
print(binary(mylist, 12))
