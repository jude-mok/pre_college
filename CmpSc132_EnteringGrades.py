#Week 3
#FINAL
def letterGrade(num): # changing to letter grade. 
  if num >= 93: 
    print(f"letter grade of class average: A")
  elif num >= 90:
    print(f"letter grade of class average: A- ")
  elif num >= 87:
    print(f"letter grade of class average: B+")
  elif num >= 83: 
    print(f"letter grade of class average: B")
  elif num >= 80:
    print(f"letter grade of class average: B- ")
  elif num >= 77:
    print(f"letter grade of class average: C+")
  elif num >= 73: 
    print(f"letter grade of class average: C")
  elif num >= 70:
    print(f"letter grade of class average: C- ")
  elif num >= 67:
    print(f"letter grade of class average: D+")
  elif num >= 63: 
    print(f"letter grade of class average: D")
  elif num >= 60:
    print(f"letter grade of class average: D- ")
  else:
    print(f"letter grade of class average: F ")


grade = 0
cuntr = 0
Invalid_Entriy_List = [] # list with invalid entries
gradeList= []
sortedGrade = []

while grade != -1 : # Putting the grade in.
  try:
    grade = float(input("Enter the grade. To quit enter \"-1\" or \"end\": "))

    if grade != -1: # making the '-1' to not get in to the list
      Invalid_Entriy_List.append(grade)
  
  except ValueError: # making while loop to quit, when the user types 'end' or 'q'
    if grade == 'end':
        break
    else:
        print("string value entered so program ended safely.")
        Invalid_Entriy_List.append('stop')
        break



print("\n")

if Invalid_Entriy_List == []:

  print("Error: No grade received so program ended")
elif 'stop' in Invalid_Entriy_List:
    try:
        Invalid_Entriy_List.pop() #poping the string 
        for i in range(len(Invalid_Entriy_List)): # making a new list with only valid entries
            if 0<= Invalid_Entriy_List[i] <= 100:
                gradeList.append(Invalid_Entriy_List[i])
                cuntr += 1
        sortedGrade = gradeList[:]
        sortedGrade.sort()
        avg = sum(gradeList)/cuntr
        mini = gradeList[0]
        maxi = gradeList[-1]
        print("-----RESULTS WITH GRADE ENTERED-----")
        print(f"Average grade: {avg}")
        print(f"Lowest grade: {mini}")
        print(f"Highest grade: {maxi}")
        print(f"Number of valid entries: {cuntr}\n")
        print(f"Entered grade(Including Invalid Entries): {Invalid_Entriy_List}")
        print(f"Entered grade(VALIDENTRIES): {gradeList}")
        print(f"Entered grade(VALID entreis and sorted version): {sortedGrade}")
        letterGrade(avg)
    
    except ZeroDivisionError: # when program is ended with str with first value
        print("pleas start again")
    
else: #Calculation
    for i in range(len(Invalid_Entriy_List)): # making a new list with only valid entries
        if 0<= Invalid_Entriy_List[i] <= 100:
            gradeList.append(Invalid_Entriy_List[i])
            cuntr += 1
    sortedGrade = gradeList[:]
    sortedGrade.sort()
    avg = sum(gradeList)/cuntr
    mini = gradeList[0]
    maxi = gradeList[-1]
    print("-----RESULTS WITH GRADE ENTERED-----")
    print(f"Average grade: {avg}")
    print(f"Lowest grade: {mini}")
    print(f"Highest grade: {maxi}")
    print(f"Number of valid entries: {cuntr}\n")
    print(f"Entered grade(Including Invalid Entries): {Invalid_Entriy_List}")
    print(f"Entered grade(VALIDENTRIES): {gradeList}")
    print(f"Entered grade(VALID entreis and sorted version): {sortedGrade}")
    letterGrade(avg)

""" no excpetions added.
while grade != -1: 
# Puting the Value to two lists (list with all the entries and list will only valid entries)

  grade = float(input("Enter the grade or to quit enter \"-1\": "))
  AllinAll.append(grade)

  if 0 <= grade <= 100:
    
    gradeList.append(grade)
    cuntr += 1


print("\n")

if gradeList == []:

  print("No grade received")

else: #Calculation

  gradeList.sort()
  avg = sum(gradeList)/cuntr
  mini = gradeList[0]
  maxi = gradeList[-1]
  print(f"Entered grade(Including Invalid Entries): {AllinAll}")
  print(f"Entered grade(Only Valid Entries): {gradeList}\n")
  print(f"Average grade: {avg}")
  print(f"Lowest grade: {mini}")
  print(f"Highest grade: {maxi}")
  print(f"Number of valid entries: {cuntr}")
  letterGrade(avg)
"""