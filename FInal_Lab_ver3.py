"""
@author: Seung Yun Mok CMPSC 132 spirng of 2023
○ Document comments

/**
 * this program is a sudoku validation code.
 **/
"""
class Sudoku:
    def __init__(self,sudoku_table) :
        self.sudoku_table = sudoku_table
        self.state_message_list = []
        self.counter = 0
        self.overall = ["----------Overall: Valid----------","----------Overall: Invalid----------"]
        self.data_checker = 0

    def displaying_sudoku(self): # display the sudokupuzzle into readable.
        print("-"*10+"SUDOKU TABLE"+"-"*10)
        for i in range(9):
            if i == 3 or i == 6:
                print("- - - - - - - - -")
            for j in range(9):
                if j == 8:
                    print(self.sudoku_table[i][j],end="\n")
                else:
                    if j % 3 == 2:
                        print(self.sudoku_table[i][j],end="|")
                    else:
                        print(self.sudoku_table[i][j],end=" ")

    def validate_duplicate_row(self,row,data_checker_row): # duplicate check process.
        if len(set(row)) == len(row):
            if data_checker_row == True:
                self.state_message_list.append(f"Row {self.sudoku_table.index(row)+1}: Valid. \nRow Info: {row}\n")
        else:
            for j in range(len(row)):
                for k in range(j+1,len(row)):
                    if row[j] == row[k]:
                        self.state_message_list.append(f"Row {self.sudoku_table.index(row)+1}: Invalid. \nNumber {row[j]} is duplicated.(Row Info:{row}).\n")
    
    def validate_row(self,row): # first of all check all the values are correct and go through the duplicate check
        n = len(row)
        data_checker_row = True
        if n != 9:
            self.state_message_list.append(f"Row {self.sudoku_table.index(row)+1}: Invalid. \nRow{self.sudoku_table.index(row)+1} has more elements than 9.(Row Info:{row}).\n")
            data_checker_row = False
        else:
            for i in range(n):
                if isinstance(row[i], int) == False:
                    self.state_message_list.append(f"Row {self.sudoku_table.index(row)+1}: Invalid. \nValue {row[i]} is not integer.(Row Info:{row}).\n")
                    data_checker_row = False
                else:
                    if row[i] < 1 or 9 < row[i]:
                        self.state_message_list.append(f"Row {self.sudoku_table.index(row)+1}: Invalid. \nNumber {row[i]} is out of range(1 to 9).(Row Info:{row}).\n")
                        data_checker_row = False
        self.validate_duplicate_row(row,data_checker_row)

    def validate_duplicate_col(self,col,data_checker_col): # duplicate check process.
        if len(set(col)) == len(col):
            if data_checker_col == True:
                self.state_message_list.append(f"Colum {self.counter}: Valid. \nColum Info:{col}\n")
        else:
            for j in range(len(col)):
                for k in range(j+1,len(col)):
                    if col[j] == col[k]:
                        state_message_col = f"Colum {self.counter}: Invalid. \nNumber {col[j]} is duplicated.(Colum Info:{col})\n" 
                        self.state_message_list.append(state_message_col)

    def validate_col(self,col): # first of all check all the values are correct and go through the duplicate check
        self.counter += 1
        n = len(col)
        data_checker_col = True
        if n != 9:
            self.state_message_list.append(f"Colum {self.counter}: Invalid. \nColum {self.counter} has more elements than 9.(Row Info:{col}).\n")
            data_checker_col = False
        else:
            for i in range(n):
                if isinstance(col[i], int) == False:
                    self.state_message_list.append(f"Colum {self.counter}: Invalid. \nValue {col[i]} is not integer.(Row Info:{col}).\n")
                    data_checker_col = False
                else:
                    if col[i] < 1 or 9 < col[i]:
                        self.state_message_list.append(f"Colum {self.counter}: Invalid. \nNumber {col[i]} is out of range(1 to 9).(Row Info:{col}).\n")
                        data_checker_col = False
        self.validate_duplicate_col(col,data_checker_col)


    def validate_duplicate_section(self,section): # duplicate check process.
        #self.counter += 1
            self.state_message_list.append =f"Section {self.counter-9}: Invalid."
            for j in range(len(section)):
                if section[j] == 0:
                    state_message_section = f"Incomplete.(Colum Info:{section})\n"
                for k in range(j+1,len(section)):
                    if section[j] == section[k]:
                        state_message_section = f"Section {self.counter-9}: Invalid. \nNumber {section[j]} is duplicated.(Colum Info:{section})\n" 
                        self.state_message_list.append(state_message_section)

    def validate_section(self,section): # first of all check all the values are correct and go through the duplicate check
        self.counter += 1
        n = len(section)
        if len(set(section)) == len(section):
            self.state_message_list.append(f"Section {self.counter-9}: Valid. \nColum Info:{section}\n")
        else:
            self.state_message_list.append(f"Section {self.counter-9}: Invalid.")
            if n != 9:
                self.state_message_list.append(f"Section {self.counter-9}: Invalid. \nSection {self.counter-9} has more elements than 9.(Row Info:{section}).\n")
            else:
                for i in range(n):
                    print(section[i])
                    if isinstance(section[i], int) == False:
                        self.state_message_list.append(f"Section {self.counter-9}: Invalid. \nValue {section[i]} is not integer.(Row Info:{section}).\n")
                        self.data_checker = 1
                    else:
                        if section[i] == 0:
                            self.state_message_list.append(f"Section {self.counter-9}: Incomplete. \n(Row Info:{section}).\n")
                        elif section[i] < 0 or 9 < section[i]:
                            self.state_message_list.append(f"Section {self.counter-9}: Invalid. \nNumber {section[i]} is out of range(1 to 9).(Row Info:{section}).\n")
                            self.data_checker = 1
            self.validate_duplicate_section(section)

    def validate_table(self): # overall divide the two dimentional list(puzzle) to row colum and section and go through the valudation function.
        self.state_message_list.append("-"*10+"ROW"+"-"*10+"\n")
        for row in self.sudoku_table:
            self.validate_row(row)

        self.state_message_list.append("-"*10+"COLUM"+"-"*10+"\n")
        for i in range(9):
            col = []
            for row in self.sudoku_table:
                col.append(row[i])
            self.validate_col(col)
            
        self.state_message_list.append("-"*10+"SECTION"+"-"*10+"\n")
        for i in range(0,9,3):
            for j in range(0,9,3):
                section = []
                for x_pointer in range(i,i+3):
                    for y_pointer in range(j,j+3):
                        section.append(self.sudoku_table[x_pointer][y_pointer])
                self.validate_section(section)



if __name__ == '__main__':
    puzzle = [ [ 7, 0, 9, 1, 2, 3, 4, 5, 6],
            [ 4, 5, 6, 7, 8, 9, 1, 2, 3],
            [ 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [ 2, 3, 4, 5, 6, 7, 8, 9, 1],
            [ 5, 6, 7, 8, 9, 1, 2, 3, 4],
            [ 8, 9, 1, 2, 3, 4, 5, 6, 7],
            [ 3, 4, 5, 6, 7, 8, 9, 1, 2],
            [ 6, 7, 8, 9, 1, 2, 3, 4, 5],
            [ 9, 1, 2, 3, 4, 5, 6, 7, 8] ]
    sudoku1 = Sudoku(puzzle)
    sudoku1.validate_table()
    sudoku1.displaying_sudoku()
    for message in sudoku1.state_message_list:
        print(message)
        

