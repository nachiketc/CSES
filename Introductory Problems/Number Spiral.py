
def findvalue(x,y):
    if x>y:
        if x%2==0:
            return x**2-(y-1)
        else:
            return (x-1)**2+y
    else:
        if y%2==0:
            return (y-1)**2+x
        else:
            return y**2-(x-1)


if __name__ == "__main__":
    t = int(input())
    output=[]
    for i in range(t):
        x,y = list(map(int,input().split(" ")))
        output.append(findvalue(x,y))
            
    for o in output:
        print(o)
   