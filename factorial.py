def factorial(n):
    res = n*1
    for i in range(1,n):
        res = res*i
        print(f"{n}! = {res}")


