#factorial 
def fact(n):
    if n==0:
        return 1
    else:
        factorial =  fact(n-1)*n
        return factorial


print(fact(100))

