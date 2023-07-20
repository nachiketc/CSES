
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split(" ")))
    moves=0
    for i in range(1,len(arr)):
        diff=arr[i-1]-arr[i] 
        if diff>0:
            arr[i]=arr[i-1]
            moves+=diff
    print(moves)