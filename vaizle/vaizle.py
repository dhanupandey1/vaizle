from datetime import timedelta, date
def fun(date1,date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

def vaizle(D):
    l=list(D)
    z= D.copy()
    D={}

    l.sort()
    x=l[0].split('-')
    a=int(x[0])
    b=int(x[1])
    c=int(x[2])
    date1 = date(a,b,c)
    x=l[len(D)-1].split('-')
    a=int(x[0])
    b=int(x[1])
    c=int(x[2])
    date2 = date(a,b,c)
    for i in range(0,len(l)-1):
        x=l[i].split('-')
        a=int(x[0])
        b=int(x[1])
        c=int(x[2])
        dt1=date(a,b,c)
        x=l[i+1].split('-')
        a=int(x[0])
        b=int(x[1])
        c=int(x[2])
        dt2 = date(a,b,c)
        s=int ((dt2 - dt1).days)
        k=0
        m=[]
        if(s>1):
            diff=z[l[i+1]]-z[l[i]]
            diff = diff/s
            k=len(m)
            for i in range(k,k+s):
               if(i==0):
                   m.append(z[l[0]])
               else:
                   sum = m[i-1]+diff
                   m.append(sum)





    p=-1
    for dt in fun(date1, date2):
        y=dt.strftime("%Y-%m-%d")
        p=p+1
        if(p<(len(m))):
            D[y]=m[p]
        else:
            D[y]=z[y]




        # print(dt.strftime("%Y-%m-%d"))
    print(D)




D = {"2019-01-01":100,"2019-01-04":115}
vaizle(D)
# print(D)
        
