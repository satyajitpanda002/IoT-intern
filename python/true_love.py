p_name = input("enter the 1st person name : ")
q_name = input("enter the 2nd person name : ")
p_name = p_name.lower()
q_name = q_name.lower()
count1 = 0 
count2 = 0

for character in p_name:
    if "true".find(character)!=-1:
        count1+=1
    if "love".find(character)!=-1:
        count1+=1

for character in q_name:
    if "true".find(character)!=-1:
        count2+=1
    if "love".find(character)!=-1:
        count2+=1

ans = count1*10 + count2

if ans<=10 or ans>=90:
    print("Your score is ",ans,", you go together like coke and mentos")
elif ans>=40 and ans<=50:
    print("Your score is ",ans,", you are alright together")
else:
    print("Your score is ",ans)