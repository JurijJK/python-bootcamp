#x = [0,1,2,3,4,5,6,7,8,9]
#y = [0,1,2,3,4,5,6,7,8,9]

print("   ", end="")
for x in range(10):
    print(f"{x:3}", end="")

print()
print()


for x in range(10):
    print(x, end="  ")
    for y in range(10):
        print(f"{x*y:3}", end="")
    print()


