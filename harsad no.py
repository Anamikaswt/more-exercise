def harsad(num):
    while num<=1000:
        digit=list(str(num))
        new=list(map(int,digit))
        if sum(new)%num==0:
            print(True)
        else:
            print(False)
        num=num+1
harsad(1)