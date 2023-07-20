

if __name__ == "__main__":

    # # Input from file
    # with open('CSES/input.txt') as f:
    #     lines = f.readlines()
    # print(lines)
    # n,x = list(map(int,lines[0].rstrip('\n').split(" ")))
    # arrP = list(map(int,lines[1].rstrip('\n').split(" ")))

    # Input from terminal 
    n,x = list(map(int,input().split(" ")))
    arrP = list(map(int,input().split(" ")))


    arrP = sorted(arrP)
    # print(arrP)
    i=0
    j=n-1
    count = 0 
    weight = 0
    while i<=j:
        # print(i,j)
        if arrP[j]+arrP[i]<=x:
            j-=1
            i+=1
            count+=1
        else:
            j-=1
            count+=1




    print(count)
