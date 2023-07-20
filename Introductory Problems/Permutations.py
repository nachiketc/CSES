
if __name__ == "__main__":
    n = int(input())
    if n%2==0:
        evenflag = True
    else:
        evenflag =False
    if n==2 or n==3:
        print("NO SOLUTION")
    elif n==1:
        print(1)
    else:
        arr = range(1,n+1)
        i=1
        while i < n:
            print(arr[i],end=" ")
            i+=2

            if evenflag:
                if i==n+1:
                    i=0
            else:
                if i==n:
                    i=0
            
           
   