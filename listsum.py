
def listsum(list):
    total = 0
    for i in range(len(list)):
        total = total+list[i]
    print(f"The sum of all items in {list} = {total}")

listsum([1,2,3,4,5])