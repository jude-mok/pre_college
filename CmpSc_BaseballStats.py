# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 15:05:10 2023

@author: skm6730
"""


condition = True
TAB, TH, TD, TT, THR, TW, TS = 0,0,0,0,0,0,0,
counter = 0
name = ""

def openingFile(fileInput):
    typeData = False
    while typeData == False:
        fileInput = fileInput + ".txt"
        try:
            fp = open(fileInput,"r")
            unsortedDataList = fp.readlines()
            fp.close()
            return unsortedDataList
        except FileNotFoundError:
            print("\nFile name not found.")
            fileInput = input("Please Enter the name of file again(Do not include \".txt\"): ")

def removingSpaceInData():
    global name
    fileName = input("Enter the name of file to organize the data of player(Do not include \".txt\"):")
    listOfData = openingFile(fileName)
    resultList1 = []
    for dataIndex in range(len(listOfData)):
        unsortedData = listOfData[dataIndex]
        unsortedData = unsortedData.split("\n")
        if dataIndex ==0:
            unsortedData.pop()
            resultList1.append(unsortedData)
        else:
            if len(unsortedData) == 2:
                unsortedData.pop()
                resultList1.append(unsortedData)
            else:
                resultList1.append(unsortedData)
    name = resultList1[0][0]
    resultList1.pop(0)
    length = len(resultList1)
    return name, resultList1, length

def convertingToInteger(dataList):
    dataList = dataList.split(",")
    for i in range(len(dataList)):
        dataList[i] = int(dataList[i])
    return dataList

def organizingData(dataListOfPlayer):
    global counter
    dataInGame = str(dataListOfPlayer[counter])
    dataInGame = dataInGame[2:-2]
    dataInGame = convertingToInteger(dataInGame)
    counter += 1
    print(f"\nWorking with game{counter}...")
    return dataInGame

def totalCalucation(battingAverage, sluggingPercentage, atBats, hits, doubles, triples, homeRuns, walks, singles):
    global TAB, TH, TD, TT, THR, TW, TS
    TAB += atBats
    TH += hits
    TD += doubles
    TT += triples
    THR += homeRuns
    TS += singles

def calculation(gameDataList):
    
    global condition
    atBats = gameDataList[0]
    hits = gameDataList[1]
    doubles = gameDataList[2]
    triples = gameDataList[3]
    homeRuns = gameDataList[4]
    walks = gameDataList[5]
    singles = hits - triples - doubles - homeRuns
    if doubles + triples + homeRuns > hits:
        battingAverage = ""
        sluggingPercentage = ""
        condition = False
        return  battingAverage, sluggingPercentage, atBats, hits, doubles, triples, homeRuns, walks, singles
    else:
        battingAverage = (hits / atBats) * 1000
        battingAverage = int(battingAverage) 
        sluggingPercentage = (((homeRuns * 4) + (triples * 3) + (doubles * 2) + singles ) / atBats) *1000
        sluggingPercentage = int(sluggingPercentage)
        totalCalucation(battingAverage, sluggingPercentage, atBats, hits, doubles, triples, homeRuns, walks, singles)
        condition = True
        return battingAverage, sluggingPercentage, atBats, hits, doubles, triples, homeRuns, walks, singles




def writingInFileWithFalse():
    global counter, name
    f = open("result.txt","a")
    if counter == 1:
        f.write("-"*10+f"Result of {name} in game{counter}"+"-"*10)
        f.write(f"\nData of player for game{counter} is wrong(sum of Doubles Triples and Home-run passed.)")
        f.write(f"\nData for game{counter} is removed")
        f.write("\n"+"-"*37)
        f.close()
    else:
        f.write("\n\n\n"+"-"*10+f"Result of {name} in Game{counter}"+"-"*10)
        f.write(f"\nData of player for game{counter} is wrong(sum of Doubles Triples and Home-run passed.)")
        f.write(f"\nData for game{counter} is removed")
        f.write("\n"+"-"*37)
        f.close()
    print(f"Problem found inside the data for game{counter}.\nPlease check the result text file.")
    

def writingInFileWithTrue(batAvg,slugPct,atBat,hit,double,triple,homerun,walk,single):
    global counter, name
    f = open("result.txt","a")
    if counter == 1:
        f.write("-"*10+f" Result of {name} in game{counter} "+"-"*10)
        f.write(f"\nBat Average: {batAvg}")
        f.write(f"\nSlugging Percentage: {slugPct}")
        f.write(f"\nAt Bat: {atBat}")
        f.write(f"\nHit: {hit}")
        f.write(f"\nSingles: {single}")
        f.write(f"\nDoubles: {double}")
        f.write(f"\nTriples: {triple}")
        f.write(f"\nHomerun: {homerun}")
        f.write(f"\nWalks: {walk}")
        f.write("\n"+"-"*52)
        f.close()
    else:
        f.write("\n\n\n"+"-"*10+f" Result of {name} in Game{counter} "+"-"*10)
        f.write(f"\nBat Average: {batAvg}")
        f.write(f"\nSlugging Percentage: {slugPct}")
        f.write(f"\nAt Bat: {atBat}")
        f.write(f"\nHit: {hit}")
        f.write(f"\nSingles: {single}")
        f.write(f"\nDoubles: {double}")
        f.write(f"\nTriples: {triple}")
        f.write(f"\nHomerun: {homerun}")
        f.write(f"\nWalks: {walk}")
        f.write("\n"+"-"*52)
        f.close()
    print(f"Successfully wrote the data for game{counter} in result txt file.")

def writingTotalStat():
    TBA = (TH/TAB) * 1000
    TSC = (((THR * 4) + (TT * 3) + (TD * 2) + TS ) / TAB) *1000
    
    TBA,TSC = int(TBA), int(TSC)
    
    f = open("result.txt","a")
    f.write("\n\n\n"+"-"*10+f" Result of {name} throughout the season "+"-"*10)
    f.write(f"\nTotal Bat Average: {TBA}")
    f.write(f"\nTotal Slugging Percentage: {TSC}")
    f.write(f"\nTotal At Bat: {TAB}")
    f.write(f"\nTotal Hit: {TH}")
    f.write(f"\nTotal Singles: {TS}")
    f.write(f"\nTotal Doubles: {TD}")
    f.write(f"\nTotal Triples: {TT}")
    f.write(f"\nTotal Homerun: {THR}")
    f.write(f"\nTotal Walks: {TW}")
    f.write("\n"+"-"*52)
    f.close()

def main():
    global condition, counter
    fN = open("result.txt","w")
    fN.close()
    name, dataListofP, numberOfGame = removingSpaceInData()
    for i in range(numberOfGame):
        dataListOfGame = organizingData(dataListofP)
        BA, SP, AB, H, D, T, HR, W, S = calculation(dataListOfGame)
        if condition == True:
            writingInFileWithTrue(BA, SP, AB, H, D, T, HR, W, S)
        if condition == False:
            writingInFileWithFalse()
    writingTotalStat()

main()

