if __name__ == "__main__":
    n = int(input())
    temp = n
    print(n,end=" ")
    flag=True
    if temp ==1:
        flag = False
    while flag:
        if temp%2==1:
            temp=temp*3+1
        else:
            temp=temp//2
        print(temp,end=" ")
        if temp==1:
            flag = False
