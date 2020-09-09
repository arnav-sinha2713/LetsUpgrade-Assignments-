def printprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
            break
        else:
            return True
lst=list(range(2501))
lst1=filter(printprime,lst)
print(list(lst1))
