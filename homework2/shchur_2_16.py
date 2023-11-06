N = int(input())
if 0 <= N <= 9999:
    if (N % 4 == 0 and N % 100 != 0) or (N % 100 != 0 and N % 400 == 0):
        print("YES")
    else:
        print("NO")
else:
    exit()
