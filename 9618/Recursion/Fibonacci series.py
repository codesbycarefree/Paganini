def RecursiveFibonacci(num):
    if num <= 1:
        return num
    else:
        return (RecursiveFibonacci(num-1)+RecursiveFibonacci(num-2))

numofterms = int(input("enter the num of terms to output"))
if numofterms <=0:
    print("Invalid input")
else:
    print("Fibonacci series:")

for i in range(numofterms):
    print(RecursiveFibonacci(i))