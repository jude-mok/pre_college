"""
@author: Seung Yun Mok CMPSC 132 spirng of 2023
○ Document comments

/**
 * this program asks user to set the range of random number and analyze the most repeated number.
 * 
 * History:
 * Seung Yun Mok, 1.0, 2023.03.23 document created
 *
 * @author Seung Yun Mok
 * @version 1.1, 2023.03.23 - Fisnished writing about function creatingList, convertingToDict, findingCount, findingMostRepeatedNumber
 
 */

○ method comments
/**
 * def creatingList(): # creating random list of numbers 
 *
 * @param : none
 * @return value : randNumbList # created random list of numbers.
 * @exception : none
 * @author : Seung Yun Mok
 * @date : 2023.03.23 
 */

/**
 * def convertingToDict(l1): # creating dictionary. keys are number in the random list, values are number of reapeat.
 *
 * @param : l1 # list of randomly selected number
 * @return value : count # dictionary created
 * @exception : none
 * @author : Seung Yun Mok
 * @date : 2023.03.23
 */

/**
 * def findingCount(d1): # get the values of the dictionary and find the biggest value.
 *
 * @param : d1 # dictionary with randomly selected numbers and the number of repeated time
 * @return value : mostCount # hishest value
 * @exception : none
 * @author : Seung Yun Mok
 * @date : 2023.03.23 
 */

/**
 * def findingMostRepeatedNumber(d2, nC): # getting the dictionary and most counted number, the function finds what number is counted the most.
 *
 * @param : d2 dictionary with randomly selected numbers and the number of repeated time, nC actual number of most repeated time
 * @return value : none
 * @exception : none
 * @author : Seung Yun Mok
 * @date : 2023.02.22 
 */
"""
import random 

counter = 0

def creatingList():
    randNumbList = []
    x, y = int(input("Enter the range(start) of random number: ")), int(input("Enter the range(end) of random number: ")) 
    length = int(input("Enter the number for the length of the list: "))
    for i in range(length):
        randomNumber = random.randint(x,y)
        randNumbList.append(randomNumber)
    return randNumbList

def convertingToDict(l1):
    count={}
    l1.sort()
    for i in l1:
        if i in count:
            count[i] += 1
        else:
            count[i]=1
    return count


def findingCount(d1):
    countList = list(d1.values())
    n = len(countList)
    mostCount = countList[0]
    for i in range(1,n):
        if mostCount < countList[i]:
            mostCount = countList[i]
    return mostCount

def findingMostRepeatedNumber(d2,nC):
    for k,v in d2.items():
      if v == nC:
        number = k
    return number

if __name__ == '__main__':
    randomlyMadeList = creatingList()
    resultDictionary = convertingToDict(randomlyMadeList)
    numberCount = findingCount(resultDictionary)
    mostRepeatedNumber = findingMostRepeatedNumber(resultDictionary,numberCount)
    print("-"*20, "result", "-"*20)
    print(f"random number list: {randomlyMadeList}")
    for k,v in resultDictionary.items():
        print(f"\nNumber of {k} repeated in random number List: {v}")
    print(f"\nMost repeated number: {mostRepeatedNumber} \nnumber of repeated times: {numberCount}")
