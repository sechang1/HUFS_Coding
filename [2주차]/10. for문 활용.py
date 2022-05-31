a = int(input())

for i in range(a):
    for k in range(a,i,-1):
        print(' ',end='')

    for k in range((i+1)*2-1):
        print("*",end='')
    print()
