import requests
import hashlib
from colorama import Fore
def main(password):

    # hash pass and seperate
    shaPassword = hashlib.sha1(password.encode()).hexdigest()
    shaPrefix = shaPassword[0:5]
    shaPostFix = shaPassword[5:].upper()



    r = requests.get(f"https://api.pwnedpasswords.com/range/{shaPrefix}", timeout=(2))
    time = str(r.elapsed).split(".")[:2]
    miliseconds = time[1][:2]


    pwned_dict = {}

    pwnd_list = r.text.split("\r\n")
    for pwned_pass in pwnd_list:
        pwned_hash = pwned_pass.split(":")
        pwned_dict[pwned_hash[0]] = pwned_hash[1]
    if shaPostFix in pwned_dict.keys():
        print(Fore.CYAN + f"  Password is not safe to use, found {{0}} instances on the internet".format(pwned_dict[shaPostFix]), Fore.MAGENTA + f"\n  Checked in: {miliseconds} miliseconds")
        return False
    else:
        print(Fore.CYAN + f"  This password is safe to use.", Fore.MAGENTA+ f"\n  Checked in: {miliseconds} miliseconds ")
        return True

if __name__ == __name__:
    main(input())
