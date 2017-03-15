'''
try:
    1/0
except ZeroDivisionError:
    pass
else :
    print("Went well!")
finally :
    print("Cleaning up.")
'''

class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry :
            print("Mmmm...")
            self.hungry = False
        else:
            print("I'm Full!")

class SongBird(Bird):
    def __init__(self):
        super(SongBird,self).__init__()
        self.Sound = 'Squawk!'
    def song(self):
        print(self.Sound)
        

bird = Bird()
bird.eat()

sb = SongBird()
sb.song()
sb.eat()
