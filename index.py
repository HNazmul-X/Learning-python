__numberDail = ["rakib", 50, 33, 22, "sabina", 39, "mim",
                "yasin", "rakib", 50,0.3, 0.4,0.0001, 33, 22, "sabina", 39,50,393,3989,1,19,29,"rakib", "ami", "sabinakevalovashi" "mim", "yasin"]


def sortSrtAndNumList(list):
    strList = []
    numList = []
    for element in list:
        if isinstance(element, str):
            strList.append(element)
        elif isinstance(element, int) or isinstance(element, float):
            numList.append(element)

    strList.sort()
    numList.sort()
    return numList+strList


print(sortSrtAndNumList(__numberDail))
