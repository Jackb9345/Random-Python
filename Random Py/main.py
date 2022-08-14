import self as self
from statistics import mode

class userInfo:
    def getDetails(self):
        userDetails = {}  # Dictionary storing user's details

        numUser = int(input("How many users would you like to add? "))

        for i in range(numUser):  # Loops once
            name = str(input("What is your name? "))
            while True:
                try:
                    age = int(input("What is your age? "))
                except ValueError:  # Checks if valid num, if not, question asked again
                    print("Not a valid number ")
                    continue
                except ZeroDivisionError:  # Checks number isn't 0
                    print("Age can't be 0")
                    continue
                break

            birthPlace = str(input("Where were you born? "))

            userDetails[name, age] = birthPlace

            print(userDetails)

    def lists(self):
        #Creating list
        birthYear = [2001, 2008, 1996, 1970, 1975, 2015]

        #Doing stuff with list
        pickFunction = str(input("1. Append 2. Insert. 3. Pop. 4. Sort"))

        if pickFunction == "1":
            appendQ = int(input("What number would you like to append? "))
            birthYear.append(appendQ)
            print(birthYear)
        elif pickFunction == "2":
            insertQ = int(input("What number would you like to insert? "))
            birthYear.insert(insertQ)
            print (birthYear)
        elif pickFunction == "3":
            birthYear.pop()
            print(str(birthYear) + " Is the new list")
        elif pickFunction == "4":
            birthYear.sort()
            print(str(birthYear) + " is the sorted list")

    def strings(self):
        keyword = "Python programming is fun"
        print(keyword)

        print(keyword[0]) #first character
        print(keyword[-2]) #second to last character

        print(keyword.upper())

        keyword.find("f")
        keyword.replace("f", "p")

        if "python" in keyword:
            print("Python is in keyword ")
        else:
            print ("Python is not in keyword ")

    def machineLearningW3(self):
        speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 86]

        #Finding mean without NumPy
        mean = (99+86+87+88+111+86+103+87+94+78+77+86) / 13
        print(mean)

        #Median without NumPy
        speed.sort() #sort numbers first
        print(speed) #Check sorted
        midPoint = len(speed) / 2 #Find length of index and half
        median = speed[int(midPoint)] #Find median using midpoint of the list "speed"
        print(median)

        #Mode
        print(mode(speed))





    #lists(self)
    #getDetails(self)
    #strings(self)
    machineLearningW3(self)