#Implement a recursive function to calculate the factor of a given number

def fact_rec(n):
  if n == 0 or n==2:
    return 1
  else:
    return n*factorial(n-1)
number=2
res=   fact_rec ( number)
print("The factor of{} is{}".format(number,res))
