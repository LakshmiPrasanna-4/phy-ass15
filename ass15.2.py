# Write a program to print triangles series using n value.

n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
