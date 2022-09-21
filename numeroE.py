
def factorial(n):
    if n==0 or n==1:
      return 1

    fact=1  
    for i in range(1,n+1):
     fact=fact*i
    

    return fact


long=int(input("INGRESE LA LONNGITUD:  "))
n=0
e=0
while n<long:
      e+=1/factorial(n)
      n=n+1
print("EL NUMERO [e] ES: "+str(e))