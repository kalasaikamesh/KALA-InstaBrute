import os
import json
from getpass import getpass
import time
import subprocess as sub
import random
import requests
import getpass
import re
from rich import print
from rich.console import Console
from rich.panel import Panel

def find_word_in_file(url, word):
    response = requests.get(url)
    if response.status_code == 200:
        file_content = response.text
        if word in file_content:
            os.system("clear")
            
            print(f'[bold green]Your id[italic blue] {word} [italic green] Has SucessFully Accepted')
            print(f"[bold white][[bold blue]✓[bold white]] [bold green]Login Sucess Full Your User Id : [italic green]{word}")
            time.sleep(5)
            pass
            
            #print(f"The word '{word}' was found in the file.")
        
    else:
        print(f"Failed to retrieve the file. Status code: {response.status_code}")
url = "https://raw.githubusercontent.com/MR-S74RK/INSTA/main/.img/users.txt"  
word_to_find = getpass.getuser() 

find_word_in_file(url,word_to_find)


# password+ banner
os.system("clear")


# BANNER educational purposes
print(Panel( '''

[bold red]●[bold yellow] ●[bold green] ●
      .---.        .-----------
     /     \  __  /    ------
    / /     \(  )/    -----
   //////   ' \/ `   ---
  //// / // :    : ---
 // /   /  /`    '--
//          //..\\\

       ====UU====UU====
           '//||\\\`
             ''``

[bold red]InstaBrute by Saikamesh sharma                          
'''))




class bcolors:
    BOLD = '\033[1m'
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[95m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'


def start():

    sceltadisc = input(
        "\033[93m\033[1m\n\n[!]Use this program  for educational purposes only? [y/n]: ")

    if sceltadisc == "y":
        print("\n")
        os.system("clear") 
        print(Panel('''
[bold red]●[bold yellow] ●[bold green] ●
      .---.        .-----------
     /     \  __  /    ------
    / /     \(  )/    -----
   //////   ' \/ `   ---
  //// / // :    : ---
 // /   /  /`    '--
//          //..\\\

       ====UU====UU====
           '//||\\\`
             ''``

[bold red]InstaBrute by WH1T3' Sai kamesh sharma

                      
'''))

    else:
        print(Panel('''
        
        Thanks for using InstaBrute 
        
        '''))
        exit()


def acquisizione():
    while True:
        if veri_break == "si":
            break
        USER = ""
        USER = input(
            '\033[1m\033[92m[?]ENTER INSTAGRAM USERNAME FOR CRACK PASSWORD: ')
        wl = input("[?]Enter the PassList along The Path: ")
        sleepp = int(
            input("\033[1m\033[91m\n[!]Type the sleep time for login(sec) (Rec:900): "))
        while True:
            sub.call("clear")
            procedere = input("Username to bruteforce = "+USER+"\n\nWordlist = "+wl+"\n\nSleep time = " +
                              str(sleepp)+bcolors.WARNING+"\n\nProoceding? [y/break/modify]: "+bcolors.ENDC)
            if procedere == "y":
                veri_break = "si"
                break
            elif procedere == "modify":
                print("\nReturn...")
                break
            elif procedere == "break":
                exit()
            else:
                pass

            
