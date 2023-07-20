
if __name__ == "__main__":
    s = input()
    currentchar = None
    maxlen = -1
    currlen = -1
    for i in range(len(s)):
        if currentchar!=s[i] or currentchar==None:
            currlen=1
            currentchar=s[i]
            
        else:
            currlen+=1

        maxlen = currlen if currlen>maxlen else maxlen

    print(maxlen)