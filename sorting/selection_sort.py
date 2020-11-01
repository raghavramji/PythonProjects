
import sys

def selection(input_l):
  print(input_l)
  for i in range(len(input_l)):
    minValue = input_l[i]
    minValuei = i
    for k in range(i, len(input_l)):
      if input_l[k] < minValue :
        minValue = input_l[k]
        minValuei = k
    t = input_l[i]
    input_l[i] = minValue
    input_l[minValuei] = t
    print(input_l)

  return input_l
print(selection([95,38,5,6,142,26])) 

