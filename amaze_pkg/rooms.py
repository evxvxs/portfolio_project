import random


class Challenge_Rooms():
    current = 0
    rooms = [0, 1, 2, 3, 4]

    def room(self, challenge):
        print(challenge)
        if self.rooms == []:
            return
        while challenge not in self.rooms:
            challenge = random.randrange(0, 5)
        self.rooms.remove(challenge)
        if challenge == 0:
            print("Challenge 0")
            print(f"""\nYou step into a room with a locked door. You need to find the key in order to progress.
The room looks very much like an average living room, but with no windows.
You see a two couches, a coffee table, and a television. There is also
an armoire, next to a fake plastic plant. There is a clock on the wall,
both hands of which are spinning rapidly and seeminlgy at random.""")
            while True:
                option = input(f"""\nWhere do you search for the key? """)
                option = option.lower()
                if option == "fake plastic plant" or option == "plastic plant" or option == "plant" or option == "fake plant":
                    print(f"""\nYou dig around in the mulch of the fake plastic plant and find the key!
You use it to unlock the door and continue through the maze.""")
                    break
                else:
                    print(
                        f"""You search the {option} for the key, but find nothing.""")
        elif challenge == 1:
            print("Challenge 1")
            print(f"""\nYou step into a room with a locked door. You need to find the key in order to progress.
The room looks very much like an average living room, but with no windows.
You see a two couches, a coffee table, and a television. There is also
an armoire, next to a fake plastic plant. There is a clock on the wall,
both hands of which are spinning rapidly and seeminlgy at random.""")
            while True:
                option = input(f"""\nWhere do you search for the key? """)
                option = option.lower()
                if option == "tv" or option == "television":
                    print(f"""\nYou search the TV and find the key taped to the back of it!
You use it to unlock the door and continue through the maze.""")
                    break
                else:
                    print(
                        f"""You search the {option} for the key, but find nothing.""")
        elif challenge == 2:
            code = random.randrange(1000, 9999)
            code = str(code)
            lights = False
            switch1 = "blue"
            switch2 = "dark"
            switch3 = "blue"
            switch4 = "dark"
            print(f"""\nYou step into a room with a locked door. You need to unlock the door in order to progress.
The room is empty aside from the ceiling which is entirely lit up with tiny LED lights.
There is also a keypad by the door, and on the other side, there are 4 switches.""")
            print(f"""\nYou have multiple input options to solve this puzzle. To press a switch, type either
'switch1', 'switch2', 'switch3', or 'switch4'. To guess the code for the door, or to enter the code when you
have discovered it, simply input the code instead of a switch option.""")
            while True:
                option = input(f"""\nSwitch 1 is {switch1}. Switch 2 is {switch2}. Switch 3 is {switch3}. Switch 4 is {switch4}.
What do you do? """)
                option = str(option.lower())
                if option == "switch1":
                    print(f"""\nYou press Switch 1.""")
                    if switch1 == "blue":
                        switch1 = "dark"
                    elif switch1 == "dark":
                        switch1 = "blue"
                    if switch2 == "blue":
                        switch2 = "dark"
                    elif switch2 == "dark":
                        switch2 = "blue"
                elif option == "switch2":
                    print(f"""\nYou press Switch 2.""")
                    if switch1 == "blue":
                        switch1 = "dark"
                    elif switch1 == "dark":
                        switch1 = "blue"
                    if switch2 == "blue":
                        switch2 = "dark"
                    elif switch2 == "dark":
                        switch2 = "blue"
                    if switch3 == "blue":
                        switch3 = "dark"
                    elif switch3 == "dark":
                        switch3 = "blue"
                elif option == "switch3":
                    print(f"""\nYou press Switch 3.""")
                    if switch2 == "blue":
                        switch2 = "dark"
                    elif switch2 == "dark":
                        switch2 = "blue"
                    if switch3 == "blue":
                        switch3 = "dark"
                    elif switch3 == "dark":
                        switch3 = "blue"
                    if switch4 == "blue":
                        switch4 = "dark"
                    elif switch4 == "dark":
                        switch4 = "blue"
                elif option == "switch4":
                    print(f"""\nYou press Switch 4.""")
                    if switch3 == "blue":
                        switch3 = "dark"
                    elif switch3 == "dark":
                        switch3 = "blue"
                    if switch4 == "blue":
                        switch4 = "dark"
                    elif switch4 == "dark":
                        switch4 = "blue"
                elif option == code:
                    print(
                        f"""\nYou input the correct code {code} into the keypad and the door opens! You progress further into the maze.""")
                    break
                else:
                    print(
                        f"""You type {option} into the keypad but nothing happens...""")
                if switch1 == "blue" and switch2 == "blue" and switch3 == "blue" and switch4 == "blue":
                    print(f"""\nAll four switches light up blue. The room instantly becomes noticabely darker as many of
the LED lights on the ceiling shut off. You look up and the only lights remaining
display the numbers {code}.""")
        elif challenge == 3:
            print("Challenge 3")
            print(f"""\nYou step into a room with a locked door. You need to unlock the door in order to progress.
There are dials on either side of the door.""")
            possible = ["dog", "cat", "fish", "star",
                        "moon", "sun", "heart", "bird", "rat"]
            slot1 = random.choice(possible)
            slot2 = random.choice(possible)
            slot3 = random.choice(possible)
            slot4 = random.choice(possible)
            slot5 = random.choice(possible)
            slot6 = random.choice(possible)
            slot7 = random.choice(possible)
            slot8 = random.choice(possible)
            print(f"""\nTheir are four dials on each side. The four on the left are locked in place.
In order, they display {slot1}, {slot2}, {slot3}, and {slot4}. The dials on
the right side spin, and currently display {slot5}, {slot6}, {slot7}, and {slot8}.
To change an image on the dial, first type the slot to change, followed by
your selection. Examples: 'slot1' then 'dog', 'slot2' then 'star', etc. The dial options are:
{', '.join(possible)}.""")
            while True:
                print(f"""\n Left Dials: {slot1} {slot2} {slot3} {slot4}
Right Dials: {slot5} {slot6} {slot7} {slot8}""")
                if slot1 == slot5 and slot2 == slot6 and slot3 == slot7 and slot4 == slot8:
                    print(
                        f"""\nWhen the right dials match the left, you hear a click and the door slides open! You progress further into the maze.""")
                    break
                option = input(f"""\nSpin a dial: """)
                option = option.lower()
                choice = option
                print(', '.join(possible))
                option = input(
                    f"""\nSelect an option from the list to adjust {choice} to: """)
                if choice == "slot1":
                    slot5 = option
                elif choice == "slot2":
                    slot6 = option
                elif choice == "slot3":
                    slot7 = option
                elif choice == "slot4":
                    slot8 = option
        elif challenge == 4:
            print(f"""\nYou step into a room with a locked door. You need to unlock the door in order to progress.
A ghostly apparition appears before you, and asks you a question....""")
            riddles = ["What has many teeth, but cannot bite?", "What has one eye, but can’t see?", "What kind of room has no doors or windows?",
                       "What is the end of everything?", "What belongs to you, but everyone else uses it?", "Take one out and scratch my head, I am now black but once was red. What am I?"]
            keys = ["comb", "needle", "mushroom", "g", "name", "match"]
            choice = random.randrange(0, 7)
            print(
                f"""The apparition asks you a question... "{riddles[choice]}" """)
            while True:
                option = input(
                    f"""\nType your answer here. Please type only one word: """)
                option = option.lower()
                if option == keys[choice]:
                    print(
                        f"""\nThe apparition smiles and disappears. You hear a click and the door slides open! You progress further into the maze.""")
                    break
                else:
                    print(
                        f"""\nThe apparition frowns. You assume this means your answer was incorrect...""")
