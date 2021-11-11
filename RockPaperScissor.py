###########################################################################################
#                                                                                         #
# A SIMPLE GAME OF ROCK PAPER SCISSOR     (An interactive python program)                 #
# I tried to make a python program of this game (somehow it is working lol)               #
# I also added a little bit decoration in this (colorama)                                 #
# In order to run this script on your computer you will need to install colorama module   #
# Open cmd and type [pip install colorama]                                                #
# https://github.com/tartley/colorama    [Check this repo ]                               #
# Feel free to tell me if you see any flaw in the script                                  #      
# Contact me on discord : Grizz#7309                                                      #
###########################################################################################




import random                                                 
import time                           
from colorama import Fore, Back, Style
############  ^ DEPENDENCIES ^  ############

comp_win = []  
user_win = []
##########  ^ EMPTY LISTS WHICH WORK AS A SCOREBOARD ^  ###########


 
def rps():
    """Rock Paper Scissor Game (Many of you know the rules but still)
Its a famous game where 2 players choose between "Rock" "Paper" "Scissor" at the same time 
-Rock gets Beaten by paper and wins against scissor
-Scissor gets beaten by rock but Wins against Paper
-Paper gets beaten by scissor but wins against rock\n\n\n"""
    chances = int(input("How many chances do you want to be in the game : "))
    for i in range(chances):
                user = input("Enter choice (rock,paper,scissor) : ") #they are cAsE SeNsiTiVE (don;t type RocK,PaPeR etc.)
                if user == "rock":
                    computer_choice = random.choice(["rock","paper","scissor"])
                    if computer_choice == "paper":
                        print(f"""{Fore.RED} Computer Win! {Fore.RESET}
-------------------------------------
You chose : {user}
Computer chose : {computer_choice}
-------------------------------------""")
                        comp_win.append(1)
                    elif computer_choice == "scissor":
                        print(f"""{Fore.GREEN} You Win ! {Fore.RESET}
-------------------------------------
You chose : {user}
Computer chose : {computer_choice}
-------------------------------------""")
                        user_win.append(1)
                    else:
                        print(f"""{Fore.YELLOW}It was a Tie {Fore.RESET}
-------------------------------------
You both have chosen : {user}
-------------------------------------""")
                elif user == "paper":
                    computer_choice = random.choice(["rock","paper","scissor"])
                    if computer_choice == "paper":
                        print(f"""{Fore.YELLOW}It was a Tie {Fore.RESET}
-------------------------------------
You both have chosen : {user}
-------------------------------------""")
                    elif computer_choice == "scissor":
                        print(f"""{Fore.RED}Computer win!{Fore.RESET}
-------------------------------------
You chose : {user}
Computer chose : {computer_choice}
-------------------------------------""")
                        comp_win.append(1)
                    else:
                        print(f"""{Fore.GREEN} You win! {Fore.RESET}
-------------------------------------
You chose : {user}
Computer chose : {computer_choice}
-------------------------------------""")
                        user_win.append(1)
                elif user == "scissor":
                    computer_choice = random.choice(["rock","paper","scissor"])
                    if computer_choice == "scissor":
                        print(f"""{Fore.YELLOW}It was a Tie {Fore.RESET}
-------------------------------------
You both have chosen : {user}
-------------------------------------""")
                    elif computer_choice == "rock":
                        print(f"""{Fore.RED}Computer win!{Fore.RESET}
-------------------------------------
You chose : {user}
Computer chose : {computer_choice}
-------------------------------------""")
                        comp_win.append(1)
                    else:
                        print(f"""{Fore.GREEN} You win! {Fore.RESET}
-------------------------------------
You chose : {user}
Computer chose : {computer_choice}
-------------------------------------""")
                        user_win.append(1)
                else:
                    print(f"{Fore.RED}Invalid Input given {Fore.RESET}")
                    time.sleep(2.0)
                    sys.stdout.write(f"Restarting the program.....\n")
                    print("\n")
                    rps()
    if len(comp_win) > len(user_win):
                print(f"{Fore.BLUE}================================================={Fore.RESET}")
                print(f"""{Fore.RED}Final Result : Computer won! 💻{Fore.RESET}
                {Fore.YELLOW} Your Score : {len(user_win)} {Fore.RESET}
                {Fore.YELLOW}Computer's Score : {len(comp_win)}{Fore.RESET}""")
                print(f"{Fore.BLUE}================================================={Fore.RESET}")
                play = input("Play Again ? [y/n] : ")
                if play == "y":
                    rps()
                elif play == "Y":
                    rps()
                elif play == "yes":
                    rps()
                elif play == "Yes":
                    rps()
                elif play == "YES":
                    rps()
                elif play == "YeS":
                    rps()
                elif play == "YEs":
                    rps()
                elif play == "yES":
                    rps()
                elif play == "yEs":
                    rps()
                elif play == "yeS":
                    rps()
                else:
                    print("Thanks for playing \n See you later 👋")
                    exit()
    elif len(comp_win) == len(user_win):
                print(f"{Fore.BLUE}================================================={Fore.RESET}")
                print(f"""{Fore.YELLOW}Final Result : Tie{Fore.RESET}
                {Fore.YELLOW} Your Score : {len(user_win)} {Fore.RESET}
                {Fore.YELLOW}Computer's Score : {len(comp_win)}{Fore.RESET}""")
                print(f"{Fore.BLUE}================================================={Fore.RESET}")
                play = input("Play Again ? [y/n] : ")
                if play == "y":
                    rps()
                elif play == "Y":
                    rps()
                elif play == "yes":
                    rps()
                elif play == "Yes":
                    rps()
                elif play == "YES":
                    rps()
                elif play == "YeS":
                    rps()
                elif play == "YEs":
                    rps()
                elif play == "yES":
                    rps()
                elif play == "yEs":
                    rps()
                elif play == "yeS":
                    rps()
                else:
                    print("Thanks for playing \n See you later 👋")
                    exit()
    else:   # Handle the case when User points are more than computer points
                print(f"{Fore.BLUE}================================================={Fore.RESET}")
                print(f"""{Fore.GREEN}Final Result : You win!🏆{Fore.RESET}
                {Fore.YELLOW} Your Score : {len(user_win)} {Fore.RESET}
                {Fore.YELLOW}Computer's Score : {len(comp_win)}{Fore.RESET}""")
                print(f"{Fore.BLUE}================================================={Fore.RESET}")
                play = input("Play Again ? [y/n] : ")
                if play == "y":
                    rps()
                elif play == "Y":
                    rps()
                elif play == "yes":
                    rps()
                elif play == "Yes":
                    rps()
                elif play == "YES":
                    rps()
                elif play == "YeS":
                    rps()
                elif play == "YEs":
                    rps()
                elif play == "yES":
                    rps()
                elif play == "yEs":
                    rps()
                elif play == "yeS":
                    rps()
                else:
                    print("Thanks for playing \n See you later 👋")
                    exit()



print(rps.__doc__)          
rps()                       
        

