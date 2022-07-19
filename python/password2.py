import random
arr_chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
arr_nums = ['1','2','3','4','5','6','7','8','9']
arr_symbols = ['!','@','#','$','%','^','&','*','(',')','[',']','{','}']

def generate(chars,numbers,symbols):
    total_len = chars+numbers+symbols
    pswd = [0]*total_len
    index_arr = [x for x in range(0,total_len)]
    # print(index_arr)
    for i in range(0,2):
        index = random.randint(0,len(index_arr)-1)
        temp = random.randint(0,len(arr_chars)-1)
        pswd[index_arr[index]] = arr_chars[temp].upper()
        index_arr.remove(index_arr[index])
    
    for i in range(0,chars-2):
        index = random.randint(0,len(index_arr)-1)
        temp = random.randint(0,len(arr_chars)-1)
        pswd[index_arr[index]] = arr_chars[temp]
        index_arr.remove(index_arr[index])

    for i in range(0,numbers):
        index = random.randint(0,len(index_arr)-1)
        temp = random.randint(0,numbers-1)
        pswd[index_arr[index]] = arr_nums[temp]
        index_arr.remove(index_arr[index])

    for i in range(0,symbols):
        index = random.randint(0,len(index_arr)-1)
        temp = random.randint(0,symbols-1)
        pswd[index_arr[index]] = arr_symbols[temp]
        index_arr.remove(index_arr[index])

    new = ""
    for x in pswd:
        new+=x
    print(new)
        


chars = int(input("enter the number of characters you want to insert (min limit is 2)"))
if chars<2:
    print("invalid input, enter correctly")
else:
    numbers = int(input("enter the number of numbers you want (min limit is 1)"))
    if numbers<1:
        print("invalid input, enter correctly")
    else:
        symbols = int(input("enter the number of symbols you want (min limit is 1)"))
        if symbols<1:
            print("invalid input, enter correctly")
        else:
            generate(chars,numbers,symbols)
