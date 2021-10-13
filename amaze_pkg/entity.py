class Entity():
    distance = 0

    def approach(self, trigger, approach):
        if trigger == True and approach == True:
            self.distance += 1
            if self.distance == 2:
                print(f"""\nYou hear a loud crash coming from far behind you, followed by a menacing roar. You get the feeling that you are now being pursued.
It would be unwise to go backwards or wait unless absolutely necessary...""")
                return False
            if 4 >= self.distance > 2:
                print(f"""\nYou can now hear the distant shuffling of whatever it is that is pursuing you, followed by the occasional howl...""")
                return False
            if 6 >= self.distance > 4:
                print(f"""\nThe shuffling has grown louder and increases in speed. You can hear the excitement in the growls of your distant pursuer echoing off the walls...""")
                return False
            if 8 >= self.distance > 6:
                print(f"""\nA terrible odor begins to penetrate your nostrils as the monstrous noises of the pursuer grow louder and louder, as if they are hot on your heels...""")
                return False
            if self.distance == 9:
                print(f"""\nThe noise no longer echoes, you can hear the entity as if they are right behind you. The terror is all consuming. You dare not wait or turn around.
You know that to do so would mean coming face to face with this monster.""")
                return False
            if self.distance == 10:
                print(
                    f"""\nA mass of swarming tentacles in the dark is the last thing that you see before everything goes dark!""")
                return True
