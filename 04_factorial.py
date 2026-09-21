#taking an input from the user
num=int(input("enter a number: "))

#initialising the fact to 1
fact=1

#loop condition
for i in range(1,num+1):
    fact=fact*i

#display result
print("Factorial of",num,"is",fact)