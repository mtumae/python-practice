def numsum(number):
    numstr = str(number)
    total = 0
    for i in range(len(numstr)):
        total = total + int(numstr[i])
    print(total)
   

numsum(123)