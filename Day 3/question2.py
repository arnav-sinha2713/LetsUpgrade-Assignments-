for i in range(1,201):
    a=int(i**0.5)
    isprime=False
    for j in range(2,a+1):
        if i%j==0:
            isprime=False
            break
        else:
            isprime=True
    if isprime==True:
        print(i)