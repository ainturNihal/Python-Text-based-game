import random
import time

from termcolor import colored

print(colored("                        THE LAST BREATH", "red", attrs=["bold"]))
print(colored('                       ------------------', "red"))
time.sleep(1)
print(colored("             Chapter One: The Beginnng of Everything", "red"))
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
shower = input("It's already 12:45pm should I take shower? (y/n): ")
if shower == "y":
  print(colored("It's better to take shower before I show up to my interview","green"))
  time.sleep(1)
  print(f"{player_name} is taking shower...")
  time.sleep(3)
  print(f"{player_name}:I....Need to know now!\nKnow now....!", 'orange'))
  time.sleep(1)
  print("Can you love me again!")
  time.sleep(1)
  print(f"{player_name} started to sing a popular song...")
  time.sleep(1)
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
  time.sleep(1)
  print(colored("You have over slept and now running late for the interview", "green"))
else:
  print(colored("Nah why should I? It ain't like a hard math exam right?","red"))
time.sleep(3)
if c == "y":
  print(colored(f"Oh no! {player_name} You are running late Hurry up!", "red"))
if c == "n":
  print(f"{player_name} stepped out to the corridor to see the mountains", 'green')
  time.sleep(3)
  print("These mountains is so stunning takes my breath everytime I look at it!")
  time.sleep(4)
  print("This view never gets old!")
  time.sleep(3)
  mount = int("Should I take a walk to the mountains? (y/n): ")
  if mount == "y":
    print("Although I might be late for the interview...")
    time.sleep(1)
    print("But how can I even ignore this stunning view?")
    time.sleep(1)
    print(colored("You took your phone, a bottle of water and went for a walk", "red"))
else:
  print("Nah,it's fine I can skip today")
  

