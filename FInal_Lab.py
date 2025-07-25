
state_message_list = []
class Sudoku:

    def __init__(self,sudoku_table) :
        self.sudoku_table = sudoku_table
    
    def displaying_sudoku(self,sudoku_table):
        self.sudoku_table = sudoku_table
        print("-"*10+"SUDOKU TABLE"+"-"*10)
        for i in range(9):
            if i == 3 or i == 6:
                print("- - - - - - - - -")
            for j in range(9):
                if j == 8:
                    print(sudoku_table[i][j],end="\n")
                else:
                    if j % 3 == 2:
                        print(sudoku_table[i][j],end="|")
                    else:
                        print(sudoku_table[i][j],end=" ")

    def validate_row(self,sudoku_table):
        self.sudoku_table = sudoku_table
        global state_message_list
        state_message_list.append("-"*10+"ROW"+"-"*10+"\n")
        for row in sudoku_table:
            if len(set(row)) != len(row):
                for j in range(len(row)):
                    for k in range(1,len(row)):
                        if j != k:
                            if row[j] == row[k]:
                                state_message_row = f"Row {sudoku_table.index(row)+1}: Invalid. \nNumber {row[j]} is duplicated.(Row Info:{row}).\n"
                                if state_message_row not in state_message_list:
                                    state_message_list.append(state_message_row)
            else:
                state_message_list.append(f"Row {sudoku_table.index(row)+1}: Valid. \nRow Info: {row}\n")
                

    def validate_col(self,sudoku_table):
        self.sudoku_table = sudoku_table
        global state_message_list
        state_message_list.append("-"*10+"COLUM"+"-"*10+"\n")
        for i in range(9):
            col = []
            for col_element in sudoku_table:
                col.append(col_element[i])
            if len(set(col)) != len(col):
                for j in range(len(col)):
                    for k in range(1,len(col)):
                        if j != k:
                            if col[j] == col[k]:
                                state_message_col = f"Colum {i+1}: Invalid. \nNumber {col[j]} is duplicated.(Colum Info:{col})\n"
                                if state_message_col not in state_message_list: #duplicated message checker.
                                    state_message_list.append(state_message_col)
            else:
                state_message_list.append(f"Colum {i+1}: Valid. \nColum Info:{col}\n")

       
            
            
puzzle = [ [ 7, 8, 9, 1, 2, 3, 4, 5, 6],
            [ 4, 5, 6, 7, 8, 9, 1, 2, 3],
            [ 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [ 2, 3, 4, 5, 6, 7, 8, 9, 1],
            [ 5, 6, 7, 8, 9, 1, 2, 3, 4],
            [ 8, 9, 1, 2, 3, 4, 5, 6, 7],
            [ 3, 4, 5, 6, 7, 8, 9, 1, 2],
            [ 6, 7, 8, 9, 1, 2, 3, 4, 5],
            [ 9, 1, 2, 3, 4, 5, 6, 7, 8] ]



def displaying_sudoku(table):
    for i in range(9):
        if i == 3 or i == 6:
            print("- - - - - - - - -")

        for j in range(9):
            if j == 8:
                print(table[i][j],end="\n")
            else:
                if j % 3 == 2:
                    print(table[i][j],end="|")
                else:
                    print(table[i][j],end=" ")



def main():
    sudoku1 = Sudoku(puzzle)
    sudoku1.displaying_sudoku(puzzle)
    sudoku1.validate_row(puzzle)
    sudoku1.validate_col(puzzle)

    for message in state_message_list:
        print(message)
        

main()