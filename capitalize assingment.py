# these code is before learning list and looping.. 
a,b,c,d = input("please enter a sentence with 4 wrods").split()
answer = a.capitalize()+b.capitalize()+c.capitalize()+d.capitalize()
print(answer)


# this code is after learning looping and list
x = input("please enter a sentence: ").split()
answer = ""
for word in x:
    answer +=  word.capitalize()

print(answer)