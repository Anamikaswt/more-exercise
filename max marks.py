def max(marks):
    i=0
    while i<len(marks):
        b=0
        m=marks[i][1]
        while b<len(marks[i]):
            num=marks[i][b]
            if num>m:
                num=m
            b=b+1
        print(num)
        i=i+1
max([[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]] )