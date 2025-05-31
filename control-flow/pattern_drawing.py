pattern = int(input("Enter the size of the pattern:" ))
rows = 0

# iterate using while
while rows <= pattern:
    for i in range(0, pattern):
        print("*",end="")
    print()
    rows += 1
    

    