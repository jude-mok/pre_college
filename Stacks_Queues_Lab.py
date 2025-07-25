#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:01:53 2023

@author: yoon
○ Document comments
/**
 * this program asks user to Create a Stack or Create a Queue Ext program. After that each data structures function(push,pop,add,remove) will work and display the result
 * 
 * History:
 * Seung Yun Mok, 1.0, 2023.02.18 document created
 *
 * @author Seung Yun Mok
 * @version 1.1, 2023.02.18 - Fisnished writing about function createStack() and stackFunction()
 */

○ method comments
/**
 * def createStack(): # creates requrire value for stackFunction
 *
 * @param : none
 * @return value : none
 * @exception : none
 * @author : Seung Yun Mok
 * @date : 2023.02.18 
 */

/**
 * def stackFunction(): # does the part of push and pop from the stack

 * @param : value,stact,countlist)
 * @return value : the result list from operation and left spaces
 * @exception : None
 * @author : Seung Yun Mok
 * @date : 2023.02.18
 *
"""


stackDirection = "3 Options with Stacks: Push, Pop, Exit."
queueDirection = "3 Options with Queue: Add, Remove, Exit."

def createStack():
    practicalStack = ["Roosevelt","Lincoln","Reagon"]
    spaceList =  [" "," "," "," "," "," "," "]
    displayStack = practicalStack + spaceList
    print("_"*100)
    print(f"\nCurrent Stack: {displayStack}")
    while True:
        inputedValue = input(f"\n{stackDirection}\nEnter a direction: ")
        inputedValue = inputedValue.lower()
        if inputedValue == "exit":
            print("\"Exit\" entered.\nThe operation ended.")
            break
        else:
            if inputedValue != "exit":
                if inputedValue == "push":
                    practicalStack, spaceLsit = stackPushOperation(displayStack,practicalStack,spaceList)
                    displayStack = practicalStack + spaceList
                elif inputedValue == "pop":
                    practicalStack, spaceLsit = stackPopOperation(displayStack,practicalStack,spaceList)
                    displayStack = practicalStack + spaceLsit

def stackPushOperation(result,stack,space):
    while True:

        nameValue = input("\nEnter the president's name or Enter \"Exit\" to stack menu: ")
        exitChecker = nameValue.lower()
            
        if exitChecker == "exit":
                return stack, space

        if len(space) == 0:
            print("\nStack is full.\nReturning to stack menu ")
            return result, space
                    
        stack.append(nameValue)
        result = stack + space            
            
        if len(result) > 10:
            space.pop()
            result = stack[:] + space
            print("\n"+"-"*50+"result"+"-"*50)
            print(f"Pushed Value: {nameValue}\nCurrent Stack: {result}")
            print("-"*106)
                    
def stackPopOperation(result2,stack2,space2):

    data = stack2[-1]
    result2 = stack2 + space2

    print(f"\nCurrent Stack: {result2}")

    direction = input(f"\nYou are going to pop \"{data}\" form the stack\nEnter \"Yes\" to pop data from stack or \"Exit\" to stack menu: ")
    while True:
        data = stack2[-1]
        if len(stack2) == 0:
            print("Stack is empty.\nReturning to stak menu ")
            return stack2,space2
                
        direction = direction.lower()

        if direction == "exit":
            print("Exit entered.\nReturning to Stack Menu")
            return stack2,space2

        elif direction == "yes":
            stack2.pop()
            result2 = stack2 + space2

            if len(result2) > 10:
                space2.pop()
                result2 = stack2 + space2
            elif len(result2) < 10:
                space2.append(" ")
                result2 = stack2 + space2

                print("\n"+"-"*50+"result"+"-"*50)
                print(f"Popped data from the string: {data}")
                print(f"Current Stack: {result2}")
                print("-"*106)

                data = stack2[-1]
                direction = input(f"\nThis time you are going to pop \"{data}\" from stack\nEnter \"Yes\" to pop {data} from stack: ")
        else:
            direction = input("Wrong input.\nPlease enter Enter \"Yes\" to pop from the stack or \"Exit\" to stack menu: ")
                    

def createQueue():
    practicalQueue = ["Pierce", "Taylor", "Rutherford"]
    spaceList2 =  [" "," "," "," "," "," "," "]
    displayQueue = practicalQueue + spaceList2
    print("_"*100)
    print(f"\nCurrent Queue: {displayQueue}")
    while True:
        inputedValueQueue = input(f"\n{queueDirection}\nEnter a direction: ")
        inputedValueQueue = inputedValueQueue.lower()
        if inputedValueQueue == "exit":
            print("\"Exit\" entered.\nThe operation ended.")
            break
        else:
            if inputedValueQueue != "exit":
                if inputedValueQueue == "add":
                    practicalQueue, spaceList2 = queueAddOperation(displayQueue,practicalQueue,spaceList2)
                    displayQueue = practicalQueue + spaceList2
                elif inputedValueQueue == "remove":
                    #practicalQueue, spaceLsit2 = stackPopOperation(displayStack,practicalStack,spaceList)
                    displayQueue = practicalQueue + spaceList2

def queueAddOperation(result3,queue,space3):
    while True:

        nameValue2 = input("\nEnter the president's name or Enter \"Exit\" to Queue menu: ")
        exitChecker2 = nameValue2.lower()
            
        if exitChecker2 == "exit":
                return queue, space3

        if len(space3) == 0:
            print("\nStack is full.\nReturning to queue menu ")
            return result3, space3
                    
        queue.insert(0,nameValue2)
        result3 = queue + space3            
            
        if len(result3) > 10:
            space3.pop()
            result3 = queue[:] + space3
            print("\n"+"-"*50+"result"+"-"*50)
            print(f"Pushed Value: {nameValue2}\nCurrent queue: {result3}")
            print("-"*106)
