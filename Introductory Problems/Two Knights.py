def findPossibilities(k):
    if k==1:
        return 0
    elif k==2:
        return 6
    else:
        return k**2*(k**2-1)//2 - 4*(k-1)*(k-2)

if __name__ == "__main__":
    n = int(input())
    for k in range(1,n+1):
        print(findPossibilities(k))
  