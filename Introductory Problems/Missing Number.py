
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split(" ")))
    missingnumber=-1
    arrsum = 0
    fullsum = sum(range(n+1))
    for i in range(len(arr)):
        arrsum+=arr[i]
    print(fullsum-arrsum)