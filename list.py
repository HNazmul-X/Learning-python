# my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

# print(*my_list)

# removedElement = my_list.pop()
# print(removedElement)
# print(my_list)

# myTuple = ("nazmul","Sabina","Mim","yasin","Tabaccum","rakib")
# myTuple = list(myTuple)
# myTuple.remove(myTuple[-1])
# myTuple = tuple(myTuple)
# print(myTuple)

myDictionary = {
    "Nazmul": "Sabina",
    "Sabina": "Nazmul",
    "Rakib": "Sabina",
    "IsSabinaLoveRakib": True,
    "isAnybodyLoveSabinaWithOutRakib": False,
    "ReletionLength": 2
}
# myDictionary2 = {
#     "family": True,
#     "mother": "Jesmin akter",
#     "Father": "Md. Abdus Samad"
# }


# dictWithFamily = {**myDictionary, **myDictionary2}
thirdDictonary = {myDictionary}
print(thirdDictonary)

# values = dictWithFamily.values()
# for data in values:
#     print(data)
