import random
arr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",'1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','[',']','{','}']

l=len(arr)
inp = input("enter y to generate a new password : ")
if inp=='y':
    res=""
    for i in range(8):
        num=random.randint(0,l)
        res+=arr[num]
    print("the password is : ",res)
else:
    print("invalid input")