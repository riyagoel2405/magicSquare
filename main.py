# -*- coding: utf-8 -*-
# Registration and Rules:
nums = [1,2,3,4,5,6,7,8,9]
userName = input("Enter Username: ")
print("Play the Magic Square Game!!\Let's go through the rules real quick:\n1. You'll have access to a list of numbers as soon as the game starts.\n2.The numbers must be placed in such a way that their sum throughout the row, column, and diagonal is the same")
print("3. By default the program asks you to enter values starting from the top-left-most and ending at bottom-right-most.\4. Should you feel a need to change the values at the end before processing, you can make use of the 'change option'.")
print("5. One number would come pre-inserted to kickstart the game.")
print("6. Best of Luck!!", userName,"\nThe available values are ", nums)

import sys
# Grid Designing
lst=[[[],[],[]],[[],[],[]],[[],[],[]]]
for i in range(1,4):
    for j in range(1,4):
      if (i,j) == (2,2):
        print( 5, end = " ")
      else:
        print("[]", end = " ")
    print()
for x in range(0,3):
  for y in range(0,3):
    if (x,y) == (1,1):
      num = 5
      lst[x][y]=num
      print("position of 5 skipped!")
    else:
      print("Enter no. for ",x+1,",",y+1,":")
      num = int(input())
      lst[x][y]=num
print("",lst[0],"\n",lst[1],"\n",lst[2])


  # Checking for sum across rows
for i in range(3):
    sumRow = 0
    for j in range(3):
      sumRow += lst[i][j]
    if sumRow == 15: 
      pass
    else:
      print("The sum in row", i, "is not 15\n You lose!!")
      sys.exit()

#Checking for sum across columns 
for i in range(3):
    sumCol = 0
    for j in range(3):
      sumCol += lst[j][i]
    if sumCol == 15:
      pass
    else:
      print("The sum in column", i, "is not 15\n You lose!!")
      sys.exit()

#Checking for sum across diagonal 1
sumDia = 0
for i in range(3):
    for j in range(3):
      if i == j:
        sumDia += lst[i][j]
if sumDia == 15:
  pass
else:
  print("Sum is not 15 in diagonal 1")
  sys.exit()

#Checking for sum across diagonal 2
sumDia = 0
for i in range(3):
    for j in range(3):
      if i+j==2:
        sumDia += lst[i][j]
if sumDia == 15:
  pass
else:
  print("Sum is not 15 in diagonal 2")
  sys.exit()
if sumDia == sumRow == sumCol:
  print("You've won!!")
