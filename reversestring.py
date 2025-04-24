def reversestring(string_input):
    reversed = []
    for i in range(len(string_input),0,-1):
        reversed.append(string_input[i-1])
    print("".join(reversed))


