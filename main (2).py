from termcolor import colored
import time
import random
print(colored("                        The last breath", "red", attrs=["bold"]))
time.sleep(2)
player_name = input(colored("\n\n\nEnter your first name: ","white"))
time.sleep(1)
print(f"{player_name}, you live in")
print(colored("Yukicho, Hiroshima in Japan","blue"))
time.sleep(2)
print("A bit far away from crowded area")
time.sleep(1)
print(f"The local people knows you as {player_name} Fuji.")
time.sleep(1)
print("You livewith your garndmother")
print(colored("Aya Fujiwa","green"))
