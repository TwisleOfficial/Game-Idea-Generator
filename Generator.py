import random

location = ['Shopping mall', 'Forest', 'Cave', 'Clouds', 'School', 'Wild west', 'Farm', 'A house', 'Underground', 'In A Ant Colony', 'In A Big City']
genre = ['Rogue', 'Battle Royal', 'FPS', 'MMO', 'RPG', 'Survival', 'Puzzle', 'Simulation', 'City Builder', 'Strategy', "Sports", 'Sandbox', 'Platformer']
goal = ['kill everything', 'escape', 'run', 'hide', 'Be the best', 'Be the worst', 'Have the best outfit', 'Destory everything', 'Build something']
rule = ['No jumping', 'No sound', 'One direction', 'Limited lives', 'No light', 'One bullet', 'Time Limit']
wildcard = ['Dark colors', 'Bright colors', 'Low-poly', 'Pixel art', 'Platformer', '2D', '3D', 'Steampunk', 'World is ending']

lines = "--------------------"

while True:
    answer = input("Generate? (y/n)")
    if answer == "y":
        print(lines)
        print("location - "+random.choice(location))
        print(lines)
        print("genre - "+random.choice(genre))
        print(lines)
        print("goal - "+random.choice(goal))
        print(lines)
        print("rule - "+random.choice(rule))
        print(lines)
        print("wildcard - "+random.choice(wildcard))
        print(lines)

        continue

    elif answer == "n":
        break
