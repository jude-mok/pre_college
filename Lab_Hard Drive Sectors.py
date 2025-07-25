
"""
Created on Tue Apr 01 20:26:10 2023

@author: Seung Yun Mok
○ Document comments
/**
 * this program is a displays the structure of linked list and how files are saved in disk.
 * 
 * History:
 * Seung Yun Mok, 1.0, 2023.04.01 document created
 *
 * @author Seung Yun Mok (CMPSC132_spring Semester of 2023)
 *
 * @version 1.1, 2023.04.01 - Fisnished program until file adding
 * @version 1.2, 2023.04.03 - Finished program numtil file removing
 * @version 1.2, 2023.04.04 - tested error cases
 *
 *
 */
 ○ method comments
 /**
    * def creating_sector(): # creates sector(disk) with basic informations
    *
    * @param : none
    * @return value : l1,empty_table # sector and basic form of showing wheter the sector is emptyor not
    * @exception : none
    * @author : Seung Yun Mok
    * @date : 2023.04.01 
*/
  
/**
    * def file_size_divider(size): # determines the number of loops
    *
    * @param : none
    * @return value : ceil(size.maxbytes)
    * @exception : none
    * @author : Seung Yun Mok
    * @date : 2023.04.01 
*/

 /**
    * def getting_info_add(): # gets input to add file.
    *
    * @param : none
    * @return value : file_name_add,file_size,hiddeness,readness # file name, # file size, #hiddeness, #readble.
    * @exception : none
    * @author : Seung Yun Mok
    * @date : 2023.04.01 
*/

/**
    * def creating_data(): # format the infos 
    *
    * @param : file_name_add,file_size,hiddeness,readness # file name, # file size, #hiddeness, #readble.
    * @return value : data_table, FS #result of format, #file size
    * @exception : none
    * @author : Seung Yun Mok
    * @date : 2023.04.01 
*/

/**
    * def adding_data(): # adds data to disk
    *
    * @param : none
    * @return value : none
    * @exception : none
    * @author : Seung Yun Mok
    * @date : 2023.04.01 
*/

/**
    * def log_add(FN): # recording logs
    *
    * @param : FN # file name
    * @return value : none
    * @exception : none
    * @author : Seung Yun Mok
    * @date : 2023.04.03 
*/

/**
    * def printing_dis(): # prints disk
    *
    * @param : FN # file name
    * @return value : none
    * @exception : none
    * @author : Seung Yun Mok
    * @date : 2023.04.03 
*/

/**
    * def removing_data(): # removes file from disk
    *
    * @param : FN # file name
    * @return value : none
    * @exception : none
    * @author : Seung Yun Mok
    * @date : 2023.04.03 
*/

/**
def log_remove(data_remove): # recording logs
    *
    * @param : data_remove # file name
    * @return value : none
    * @exception : none
    * @author : Seung Yun Mok
    * @date : 2023.04.03 
*/

/**
def printing_log(): # print logs
    *
    * @param : none 
    * @return value : none
    * @exception : none
    * @author : Seung Yun Mok
    * @date : 2023.04.03 
*/

/**
def menu(): # starts program
    *
    * @param : none
    * @return value : none
    * @exception : none
    * @author : Seung Yun Mok
    * @date : 2023.04.03 
*/

 *
""" 

import math

def creating_sector():
    l1,empty_table = [], ["EMPTY","-1","-1","",0]
    for i in range(0,21):
        l1.append(empty_table)
    return l1, empty_table

maxbytes = 500
max_capacity_of_bytes = 10000
sector, basic_info = creating_sector()
condition = True
log_book_name = []
log_message = []

def file_size_divider(size):
    global maxbytes
    return math.ceil(size/maxbytes)

def getting_info_add():
    global condition, maxbytes, max_capacity_of_bytes
    condition = True
    file_name_add = input("\nEnter file name: ")

    file_size = input("\nEnter the size of file in bytes(Max: 10000): ")
    while condition == True:
        try:
            file_size = int(file_size)
            if file_size >= 1 and file_size <= 10000:
                max_capacity_of_bytes -= file_size
                condition = False
            else:
                file_size = input("\nWrong Input(file size out of range). \nEnter the size of file in bytes again(Max: 10000): ")
        except ValueError:
            file_size = input("\nWrong Input(input was not integer). \nEnter the size of file in bytes again(Max: 10000): ")
    
    hiddeness = input("\nEnter the T/F to determine whether file is hidden or not: ")
    while condition == False:
        if hiddeness == "T":
            hiddeness = "H"
            condition = True
        elif hiddeness == "F":
            hiddeness = "h"
            condition = True
        else:
            hiddeness = input("\nWrong Input. \nEnter the T/F to determine whether file is hidden or not: ")

    condition = False

    readness = input("\nEnter the T/F to determine whether file is readable or not: ")
    while condition == False:
        if readness == "T":
            readness = "R"
            condition = True
        elif readness == "F":
            readness = "r"
            condition = True
        else:
            readness = input("\nWrong Input. \nEnter the T/F to determine whether file is readable or not: ")       
    return file_name_add,file_size,hiddeness,readness

def creating_data(FNA,FS,H,R):
    if FS > 500:
        data_table = [FNA,"500",H,R]
        FS -= 500
    else:
        data_table = [FNA,str(FS),H,R]
    data_table = "-".join(data_table)
    return data_table, FS

def adding_data(): 
    global sector, condition, basic_info
    dummy_pointer = []
    name_of_file, size_of_file, hide, read = getting_info_add()
    repeating_number = file_size_divider(size_of_file)

    for i in range(repeating_number):

        file_data_string, size_of_file = creating_data(name_of_file,size_of_file,hide,read)
        empty_find = sector.index(basic_info)
        sector[empty_find] = dummy_pointer
        next_pointer =  empty_find+1
        previous_pointer = -1
        
        if i != 0: # first appending data -> prev pointer -1 fixed.
            previous_pointer = next_pointer-2
            if sector[empty_find-1][3] != name_of_file:
                previous_pointer = sector.index(file_data_list)
        if sector[empty_find+1] != basic_info:
            next_pointer = sector.index(basic_info)
        if i == repeating_number-1: 
            next_pointer = -1
        file_data_list = [file_data_string,next_pointer,previous_pointer,name_of_file,size_of_file]
        sector[empty_find] = file_data_list

    log_add(name_of_file)

def log_add(FN):
    global log_message, log_book_name
    log_book_name.append(FN)
    log_message_add = f"{FN} added to disk."
    log_message.append(log_message_add)
        
def printing_disk():
    global sector
    print("\n"+"-"*10 + "Current Disk" + "-"*10)
    print("   info of file        |   next  |  previous")
    for j in range(len(sector)-1):
        if j < 10:
            print(f"{j}) {sector[j][0]}                 {sector[j][1]}       {sector[j][2]}")
        else:
            print(f"{j}){sector[j][0]}                  {sector[j][1]}       {sector[j][2]}")

def removing_data():
    global sector, max_capacity_of_bytes
    file_name_remove  = input("\nEnter the file name to remove: ")
    counter = 1
    for i in range(len(sector)):
        if sector [i][3] == file_name_remove:
            if counter == 1:
                max_capacity_of_bytes += sector [i][4]
                counter += 1
            sector [i] = ["EMPTY","-1","-1","",0]
    log_remove(file_name_remove)

def log_remove(data_remove):
    global log_message, log_book_name
    if data_remove in log_book_name:
        log_message_remove = f"{data_remove} removed from disk"
    else:
        log_message_remove = f"File name \"{data_remove}\" was not found"
    log_message.append(log_message_remove)

def printing_log():
    global log_message
    print("\n"+"-"*10+"log"+"-"*10)
    for i in range(len(log_message)):
        print(log_message[i])
    print("-"*23+"\n")

def menu():
    global condition, max_capacity_of_bytes,sector,basic_info
    
    menuList = ["Add","Remove","Exit"]
    direction = 0
    

    while condition == True:
        print("-"*10+"Operation Start"+"-"*10+"\n")
        for i in range(3):
            print(f"{i+1}) {menuList[i]}") 
        try:
            direction = int(input("\nEnter a number to choose direction: "))
            if 3 < direction or 1 >direction:
               direction = input(f"Wrong Input(input out of range). \nEnter the direction by entering the number in front of direction again: ")
            else:
                if direction == 1:
                    if max_capacity_of_bytes < 499:
                        print("Disk is full. \nProgram Ends.")
                        condition = False
                    else:
                        adding_data()
                        printing_disk()
                        printing_log()
                elif direction == 2:
                    if sector[0][0] == "EMPTY":
                        direction = input("\nError: DISK IS EMPTY\nEnter a number to choose direction: ")
                    else:
                        removing_data()
                        printing_disk()
                        printing_log()
                else:
                    print(f"{direction} was inputed.\nProgram ended")
                    condition = False
        except ValueError:
            print("\nWrong Input(something else,not integer typed).")

if __name__ == '__main__':
    menu()