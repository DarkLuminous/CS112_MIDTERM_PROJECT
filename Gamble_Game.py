from ast import Global
import os
import random
from time import sleep
from tkinter import END
from turtle import clear

NumberToGuess = 0
playAgain = 0
Again = 0
Money = 100
betMoney = 0
GuessedNumber = 0

#=========================================================================        
#text art
zEro = "=========\n   000\n  0   0\n  0   0\n  0   0\n   000\n========="
    #print(zero)

oNe = "=========\n    1\n   11\n    1\n    1\n   111\n========="
        #print (one)

tWo = "=========\n   222\n  2   2\n     2\n    2\n  22222\n========="
        #print(two)

thRee = "=========\n   333\n  3   3\n    33\n  3   3\n   333\n========="
        #print(three)

fOur = "=========\n   444\n  4  4\n  4  4\n  44444\n     4\n========="
        #print(four)

fIve = "=========\n  5555\n  5\n  555\n     5\n  555\n========="
        #print(five)

sIx = "=========\n   666\n  6    \n  6666\n  6   6\n   666\n========="
        #print(six)

seVen = "=========\n  77777\n     7\n    7\n   7\n   7\n========="
        #print(seven)

eiGht = "=========\n   888\n  8   8\n   888\n  8   8\n   888\n========="
        #print(eight)

nIne = "=========\n   999\n  9   9\n   9999\n      9\n   999\n========="
    
        #print(nine)

#============================================================================

def Play_Gamble():
    global Money
    global NumberToGuess

    
    print("WELCOME TO GAMBLE!")
    print(f"MONEY: {Money}$")
    NumberToGuess = (random.randrange(1, 9))                    #GENERATE A RANDM NUMBER 1 - 9
    print("Press ENTER to Continue . . .")
    Cheat = input()
    
    if Money == 0:
      End_game()   
 
#********CHEATS*************************
      
    if Cheat == "cheat1":
      print(NumberToGuess)
      sleep(1)
      
    elif Cheat == "money100":
      print("+100$") 
      sleep(1)
      
#****************************************

    os.system('cls')
    First_Phase()
     
def First_Phase():
    global GuessedNumber
    
    while True:  #Loop this Phase until other Phase is called
     print("Range from 1 to 9")
     print("What's your number? NUMBER:")       
     GuessedNumber = input()
     
     InpCheck = GuessedNumber.isdigit() #check input if number if valid
     
     if InpCheck == False:
      print("Numbers Only Please!")
      sleep(1)
      os.system('cls')
      
     elif 10 <= int(GuessedNumber):
      print("your number is too high!")
      sleep(1)
      os.system('cls')                 
      
     elif 0 >= int(GuessedNumber):
      print("your number can't be zero")
      sleep(1)
      os.system('cls')
      
     else:
      Second_Phase() #proceed to 2nd_Phase
      sleep(1)
      os.system('cls')
      
def Second_Phase():
    global betMoney
    
    while True:
     print(f"Your Ramaining Money is: {int(Money)}$")
     print("How Much you want To Bet? BET:")
          
     betMoney = input()
     
     InpCheck = betMoney.isdigit()                      
     
     if InpCheck == False:
      print("Numbers Only Please!")
      sleep(1)
      os.system('cls')
     elif int(betMoney) > int(Money):
      print("You don't have enough MONEY!")
      sleep(1)
      os.system('cls')
     else:
      Third_Phase()
      os.system('cls')

def Third_Phase():
    

    
    while True:
     print(f"Your GUESSED NUMBER is: {GuessedNumber}")
     print(f"And BET: {betMoney}$")
     print("WOULD YOU LIKE TO CHANGE YOUR GUESSED NUMBER AND BET? 1:YES|2:NO")

     Again = input()    
     
     InpCheck = Again.isdigit()                        
     
     if InpCheck == False:
      print("Numbers Only Please!")
                            
     elif int(Again) < 1 or int(Again) > 2:
      print("Invalid Number, please enter 1 for YES or 2 for NO.")

     elif int(Again) == 1:
      os.system('cls')
      print("Wait for a seconds")
      sleep(1)
      os.system('cls')
      First_Phase()
      
     elif int(Again) == 2:
      os.system('cls')
      print("Wait for a seconds")
      sleep(1)
      Final_Phase()
     
def Final_Phase():
 global betMoney
 global Money

#*********TEXT ART**************************
 if int(NumberToGuess) == 0:
      Dis_NumberToGuess = zEro
 elif int(NumberToGuess) == 1:
      Dis_NumberToGuess = oNe
 elif int(NumberToGuess) == 2:
      Dis_NumberToGuess = tWo
 elif int(NumberToGuess) == 3:
      Dis_NumberToGuess = thRee
 elif int(NumberToGuess) == 4:
      Dis_NumberToGuess = fOur
 elif int(NumberToGuess) == 5:
      Dis_NumberToGuess = fIve
 elif int(NumberToGuess) == 6:
      Dis_NumberToGuess = sIx
 elif int(NumberToGuess) == 7:
      Dis_NumberToGuess = seVen
 elif int(NumberToGuess) == 8:
      Dis_NumberToGuess = eiGht
 elif int(NumberToGuess) == 9:
      Dis_NumberToGuess = nIne 
#********************************************

 if int(GuessedNumber) == int(NumberToGuess):               #WON output
  
  os.system('cls')
  Money = (int(betMoney) * 2 )
  print("YOU WON!")
  print(f"Your Money Increase by: {Money}$")
  
  Play_Gamble_Again()
  
 else:
  Money = (int(Money) - int(betMoney))                      #Lose output
  
  print("You Lose!")
  print(f"The Answer is:\n{Dis_NumberToGuess}")
  print(f"Your Money Deducted, Now you have only:{int(Money)}$")  

  Play_Gamble_Again()
  
def Play_Gamble_Again():

 while True:
  print("Want to play Again? 1:yes|2:no")               
  Again = input()
  InpCheck = Again.isdigit()
                    
  if InpCheck == False:
    print("Numbers Only Please!")
                            
  elif int(Again) < 1 or int(Again) > 2:
    print("Invalid Number, please enter 1 for yes or 2 for no.")

  elif int(Again) == 1:
    os.system('cls')
    print("Wait for a seconds")
    sleep(2)
    os.system('cls')
    Play_Gamble()
                            
  elif int(Again) == 2:
      End_game()              
      
def End_game():
      
      if Money == 0:
         print("You Dont have enough Money to Continue playing")         #output if 0 Money
    
      print("Thank you For Playing!")
      sleep(1)
      os.system('cls')
      
      print("The_Gamble by Roger Bao Jr. And Hakima Abdulkarim")
      sleep(1)
      exit()                                                              #END
   
      
Play_Gamble()
