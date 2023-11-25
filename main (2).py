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
time.sleep(1)
print(colored("You never met your parents", "red"))
time.sleep(1)
print("Just today you have got an offer from a nearby restrurent called Yakiniku Suuchan, and today at 5:30pm you have to go for that interview")
time.sleep(3)
print(f"{player_name} Thinking...")
c = input("It's already 12:45pm should I take shower? (y/n): ")
if c == "y":
  print(colored("It's better to take shower before I show up to my interview","green"))
else:
  print(colored("Nah, I am plenty cool these showers don't matter to me I am always the best","red"))
  print(colored("HAHA!", "red"))
time.sleep(3)
time = random.randint(9,58)
print(f"2:{time}")
time.sleep(3)
print(f"{player_name} Thinking...")
c = input("Should i take a nap before the interview? (y/n): ")
if c == "y":
  print(colored("I should clear my mind before an interview","green"))
else:
  print(colored("Nah why should I? It aint like a hard math exam right?","red"))
time.sleep(3)
ptint("Nit finished...")


