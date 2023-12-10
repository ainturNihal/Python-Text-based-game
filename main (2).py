import random
import time

from termcolor import colored
print("This game is recomended to play in PC/Laptop\nAS some arts may not appea as it was intented in mobile")
print(colored("                        THE LAST BREATH", "red",
              attrs=["bold"]))
print(colored('                       ------------------', "red"))
time.sleep(1)
print(colored("             Chapter One: The Beginnng of Everything", "red"))
time.sleep(2)
player_name = input(colored("\n\n\nEnter your first name: ", "white"))
time.sleep(1)
print(f"{player_name}, you live in")
print(colored("Yukicho, Hiroshima in Japan", "blue"))

time.sleep(2)
print("A bit far away from crowded area")
time.sleep(1)
print(f"The local people knows you as {player_name} Fuji.")
time.sleep(1)
print("You live with your garndmother Aya Fujiwa in this house")
time.sleep(2)

#asci art from google


print('''                                                    ___
                                             ___..--'  .`.
                                    ___...--'     -  .` `.`.
                           ___...--' _      -  _   .` -   `.`.
                  ___...--'  -       _   -       .`  `. - _ `.`.
           __..--'_______________ -         _  .`  _   `.   - `.`.
        .`    _ /\    -        .`      _     .`__________`. _  -`.`.
      .` -   _ /  \_     -   .`  _         .` |   Japan!  |`.   - `.`.
    .`-    _  /   /\   -   .`        _   .`   |___________|  `. _   `.`.
  .`________ /__ /_ \____.`____________.`     ___       ___  - `._____`|
    |   -  __  -|    | - |  ____  |   | | _  |   |  _  |   |  _ |
    | _   |  |  | -  |   | |.--.| |___| |    |___|     |___|    |
    |     |--|  |    | _ | |'--'| |---| |   _|---|     |---|_   |
    |   - |__| _|  - |   | |.--.| |   | |    |   |_  _ |   |    |
 ---``--._      |    |   |=|'--'|=|___|=|====|___|=====|___|====|
 -- . ''  ``--._| _  |  -|_|.--.|_______|_______________________|
`--._           '--- |_  |:|'--'|:::::::|:::::::::::::::::::::::|
_____`--._ ''      . '---'``--._|:::::::|:::::::::::::::::::::::|
----------`--._          ''      ``--.._|:::::::::::::::::::::::|
`--._ _________`--._'        --     .   ''-----.................'
     `--._----------`--._.  _           -- . :''           -    ''
          `--._ _________`--._ :'              -- . :''      -- . ''
 -- . ''       `--._ ---------`--._   -- . :''
          :'        `--._ _________`--._:'  -- . ''      -- . ''
  -- . ''     -- . ''    `--._----------`--._      -- . ''     -- . ''
                              `--._ _________`--._
 -- . ''           :'              `--._ ---------`--._-- . ''    -- . ''
          -- . ''       -- . ''         `--._ _________`--._   -- . ''
:'                 -- . ''          -- . ''  `--._----------`--._''')




time.sleep(1)
print(colored("\n\n\n\n\n\nYou never met your parents", "red"))
time.sleep(1)
print("\nJust today you have got an offer from a nearby restrurent called Yakiniku Suuchan.")
print("\nToday at 5:30pm you have to go for that interview")
time.sleep(3)
print(f"{player_name} Thinking...")
shower = input("It's already 12:45pm should I take shower? (y/n): ")
if shower == "y":
  print(colored("It's better to take shower before I show up to my interview","green"))
  time.sleep(1)
  print(f"{player_name} is taking shower...")
  time.sleep(3)
  print(colored(f"{player_name}:I....Need to know now!\nKnow now....!", 'green'))
  time.sleep(1)
  print("Can you love me again?!")
  time.sleep(1)
  print(f"{player_name} started to sing a popular song...")
  time.sleep(1)
  print(f"After nearly 4 min of singing along {player_name} was done with his shower.")
else:
  print(colored("Nah, I am plenty cool these showers don't matter to me I am always the best","red"))
  print(colored("HAHA!", "red"))
time.sleep(3)

print("You took a nap before going for your interview...\n")
time.sleep(3)
print(colored("You are running late for your interview","red"))
print("You rapidly got ready and headed for your interview by your cycle\n\n\n")
time.sleep(4)
print(colored("You arrived at your interview","red"))
print("You entered the resturant and the gust of a delecious food blew you")
time.sleep(1)
print("Moment letter a beautiful girl walked towards you and asked for your name")
time.sleep(1)
print("You replied with your name")
time.sleep(1)
print("She smiled and said")
time.sleep(1)
print(colored('My name is Ayame!','light_blue'))
time.sleep(1)
print("Then she told you to sit inside")
time.sleep(1)
print("Youwent inside and an old man came and stared at you for a few seconds")
time.sleep(2)
print(colored("The old man: My name is Isamu, I am the manager of the resturant.","light_blue"))
time.sleep(1)
car = input(colored("Isamu: Do you have any car?", 'green'))
if car == "yes":
  print(colored("Isamu: Yes, I have a Honda Civic.","light_blue"))
  time.sleep(1)
  print("Isamu: Oh, I thought you do not have a car as you did not bring one.")
else:
  print("Isamu: Oh, that is why you brought a cycle, I see")

print("Isamu: So, are you from around here?")
q1 = input(''''a) I am from Tokyo.
               b) I am an alien!
               c) I am from here, Hiroshima.
               d) I am from S.Korea.''')
if q1 == c:
  print(colored("Well that's one thing we have in common!", 'green'))
else:
  time.sleep(1)
  print(colored("But I heard that you are from Hiroshima.", 'red'))
  time.sleep(1)
  print(f"{player_name}: My bad, Sleep of toung")
  print(colored("[Isamu is slowly fuming]", 'red'))
  time.sleep(1)
  print("Isamu: You have to be more careful as it is your interview.")
  print(f"{player_name}: My appoligies...")
  
time.sleep(2)
print("Isamu: Before I give you the job are you able to do hard work?")
q2 = input('''a)The fuck you mean? Why would I do hard work?
              b) Meh, I will think about it
              c) Depends on my mood.
              d)Yes, I am willing to do whatever it takes to do!''')

if q2 == d:
  print("Isamu: Well, I am glad to hear that.")
if q2 == a:
  print(colored("Isamu: How dare you speak to your elders like that!?", 'red'))
  time.sleep(1)
  print(colored("GET OUT OF MY PROPERTY NOW!",'red'))
  print(f"{player_name}: Sheesh Old man you gonna get a heart attack")


