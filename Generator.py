import random

location = ['shopping mall', 'forest', 'cave', 'cloud', 'school', 'wild west']
genre = ['rogue', 'battle royal', 'FPS', 'MMO', 'RPG', 'survival']
goal = ['kill everything', 'escape', 'run', 'hide', 'farm']
rule = ['no jumping', 'no sound', 'one direction', 'limited lives']
wildcard = ['dark colors', 'bright colors', 'low-poly', 'pixel art', 'platformer']

while True:
    answer = input("Generate? (y/n)")
    if answer == "y":
        print("--------------------")
        print("                    ")
        print("location - "+random.choice(location))
        print("genre - "+random.choice(genre))
        print("goal - "+random.choice(goal))
        print("rule - "+random.choice(rule))
        print("wildcard - "+random.choice(wildcard))
        print("                    ")
        print("--------------------")

        continue

    elif answer == "n":
        break
