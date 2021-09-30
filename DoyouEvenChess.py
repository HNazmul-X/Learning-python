# function for checking 2 lenght Element
def checkingLen2(check):
    isValid = check[0].islower()
    if isValid:
        isValid = check[1].isnumeric()
    return isValid

# function for Checking 3 Length Check
def checkingLen3(check):
    def type1():
        if checkingLen2(check[0]+check[1]):
            return check[2] == "#" or check[2] == "+"
        else:
            return False

    def type2():
        if check[0].isupper():
            lastTow = check[1]+check[2]
            if checkingLen2(lastTow):
                return True
        else:
            return False
            
    def type3():
        if check == "O-O":
            return True
        else:
            return False

    if type1() == True:
        return type1()
    elif type2() == True:
        return type2()
    elif type3() == True:
        return type3()
    else:
        return False


# function for checking 4 length of move
def checkingLen4(check):
    def type1():
        if checkingLen3(check[0]+check[1]+check[2]):
            return check[3] == "#" or check[3] == "+"
        else:
            return False

    def type2():
        isvalid = check[0].islower() and check[1] == "x"
        if isvalid:
            if checkingLen2(check[2]+check[3]):
                return True
            else:
                return False
        else:
            return False

    def type3():
        isvalid = check[0].isupper()

        if isvalid:
            if check[2].islower():
                isvalid = True
            elif check[2].isnumeric():
                isvalid = True
            else:
                isvalid = False

        if isvalid:
            if checkingLen2(check[2]+check[3]):
                return True
            else:
                return False
        else:
            return False

    if type1() == True:
        return type1()
    elif type2() == True:
        return type2()
    elif type3() == True:
        return type3()
    else:
        return False


def checkingForValidMove(lst):
    if isinstance(lst, list):
        if lst[-1][-1] == "#":

            isValidMove = False

            # looping list element
            for move in lst:
                if len(move) == 2:
                    isValidMove = checkingLen2(move)
                    if isValidMove == False:
                        break
                elif len(move) == 3:
                    isValidMove = checkingLen3(move)
                    if isValidMove == False:
                        break
                elif len(move) == 4:
                    isValidMove = checkingLen4(move)
                    if isValidMove == False:
                        break
                e
            if isValidMove:
                return "valid"
            else:
                return "Invalid"
        else:
            return "invalid"
    else:
        return "your Enterd Value is not a List"


allListedMove = "e4 c5 Nf3 d6 Nbxd7 O-O d7#".split()
print(checkingForValidMove(allListedMove))
