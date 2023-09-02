def factorial():
  num = int(input("Enter a number: "))    
  f = 1    
  if num < 0:    
    print("Factorial does not exist for negative numbers")    
  elif num == 0:    
    print("The factorial of 0 is 1")    
  else:    
    for i in range(1,num + 1):    
       f = f*i    
    print("The factorial of",num,"is",f)    

#factorial(10,1)
factorial()
