rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random 
signs_list = [rock, paper, scissors]
your_choice = int (input ("Chose ¨0¨ for rock, ¨1¨ for paper, ¨2¨ for sciccors: \n")) 
print ("You chose: \n" + signs_list [your_choice])


#computers coice
computers_choice = random.randint (0,len (signs_list) - 1) 
print ("Computer chose: \n" + signs_list [computers_choice]) 

#evaluating 
if (your_choice == 0 and computers_choice == 2) or (your_choice == 2 and computers_choice == 1) or (your_choice == 1 and computers_choice == 0): 
  print ("You win!")
elif (your_choice == 2 and computers_choice == 0) or (your_choice == 1 and computers_choice == 2) or (your_choice == 0 and computers_choice == 1):
  print ("Computer wins!")
else :
   print ("It is a draw. Nobody wins!")