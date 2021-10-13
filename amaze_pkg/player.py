import random
print(f"""\nYou step into a room with a locked door. You need to unlock the door in order to progress.
A ghostly apparition appears before you, and asks you a question....""")
riddles = ["What has many teeth, but cannot bite?", "What has one eye, but can’t see?", "What kind of room has no doors or windows?",
           "What is the end of everything?", "What belongs to you, but everyone else uses it?", "Take one out and scratch my head, I am now black but once was red. What am I?"]
keys = ["comb", "needle", "mushroom", "g", "name", "match"]
choice = random.randrange(0, 7)
print(riddles[choice])
print(keys[choice])
