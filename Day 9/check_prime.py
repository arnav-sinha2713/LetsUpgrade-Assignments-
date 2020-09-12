'''
It is a checkprime module
'''
def checkprime(num):
    '''
    It is a checkprime function
    '''
    result=False
    for i in range(2,num):
        if num%i==0:
            result=False
            break
        else:
            result=True
    if result==True:
        return True
    else:
        return False

print(checkprime(57))
