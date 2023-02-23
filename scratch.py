def calculator(a,b,op):
    ans=0
    if op==1:
        ans=add(a,b)
    elif op==2:
        ans=subtract(a,b)
    elif op==3:
        ans=mul(a,b)
    elif op==4:
        ans=div(a,b)
    else:
        print("Incorrect input")

    print("Output for the given operation is: ",ans)

a=input("Enter first value: ")
b=input("Enter the second value: ")
print()
print("1:add, 2:subtract, 3:multiplication, 4: division")
op=input("Enter your choice for operation: ")
calculator(a,b,op)