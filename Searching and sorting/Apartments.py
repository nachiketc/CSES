

if __name__ == "__main__":

    # # Input from file
    # with open('CSES/input.txt') as f:
    #     lines = f.readlines()
    # print(lines)
    # n,m,k = list(map(int,lines[0].rstrip('\n').split(" ")))
    # arrA = list(map(int,lines[1].rstrip('\n').split(" ")))
    # arrB = list(map(int,lines[2].split(" ")))

    # Input from terminal 
    n,m,k = list(map(int,input().split(" ")))
    arrA = list(map(int,input().split(" ")))
    arrB = list(map(int,input().split(" ")))

    # print(arrA,arrB)

    arrA=sorted(arrA)
    arrB=sorted(arrB)
    # print(arrA,arrB)

    i=j=0
    count = 0 
    while i<len(arrA) and j<len(arrB):
        if arrB[j]<=arrA[i]+k and arrB[j]>=arrA[i]-k:
            i+=1
            j+=1
            count+=1
        elif arrB[j]<arrA[i]+k:
            j+=1
        else:
            i+=1




    print(count)
