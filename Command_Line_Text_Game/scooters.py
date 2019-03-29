# Welcome to Theodore Fong's game called 'A Night at Scooters'

# import sys and random.random
import sys
from random import random

# Base class which represents the user
class person:

    def __init__(self, name):
        """Initial variables"""

        self.name = name
        self.fun_lvl = 0
        self.drink_lvl = 0
        self.time = 0
        self.luck = 0.05

    def drink(self, drink_number):
        """Takes a drink and adds to your drink_lvl to calculate your
        BAC. Then, calculates luck based upon how high your BAC is. As luck
        increases, the outcomes of each activity becomes more extreme since
        when people get drunk, their actions tend to become really good or
        bad, but hardly in between.
        """

        self.drink_lvl += (0.03 * drink_number)

        # luck cannot be greater than 0.5
        if self.drink_lvl < 0.3:
            self.luck = self.drink_lvl // 0.03 * 0.05
            print("Your BAC is currently {:.2f} ".format(self.drink_lvl)
                  + "and your luck is {:.2f}".format(self.luck))

        # if BAC > 0.3, then you are drunk and the game ends by speeding time
        # by 360 minutes in order to exit the while loop forthe game() method.
        # 360 is valid because the game simulates a 6 hour period.
        else:
            self.fun(0, 0)
            self.time += 360

    def get_time(self, change):
        """Records how long the night has been and presents the time in
        military time format. This function will also sober you one drink for
        every hour once you are drinking.
        """

        # time is measured in minutes
        self.time += change

        # sobers up BAC by one drink every hour, but only if time is exactly
        # a multiple of 60. This simulates how sometimes we expect to sober
        # up, but do not due to unforeseen circumstances
        if self.time % 60 == 0 and self.drink_lvl >= 0.03:
            self.drink_lvl -= 0.03
        else:
            None

        # translates time into military time between 2000 - 0200.
        minutes = self.time % 60
        if (self.time / 60) < 4:
            hour = (self.time // 60) + 20
        else:
            hour = (self.time // 60) - 4
        return str("{:02d}{:02d}".format(hour, minutes))

    def fun(self, fun_change, time_change=5):
        """Measures changes in the fun level and displays the status of
        how much time has passed and what your current fun level is.
        """

        # fun_level must be between 0 and 100
        if self.fun_lvl + fun_change > 100:
            self.fun_lvl = 100
        elif self.fun_lvl + fun_change < 0:
            self.fun_lvl = 0
        else:
            self.fun_lvl += fun_change

        # changes time based upon the activity through the get_time method
        new_time = self.get_time(time_change)

        print("--------Status-------- \n"
              + "The time is {} ".format(new_time)
              + "and your fun level is {}".format(self.fun_lvl))

    def end_night(self):
        """This method will end the night and display how you performed."""

        # Adjusts fun level based upon how BAC at the end of the night
        print("--------Summary--------")
        if 0.3 <= self.drink_lvl:
            print("You go to the hospital due to alcohol poisoning. Fun -100")
        elif 0.08 <= self.drink_lvl < 0.3:
            self.fun_lvl -= 20
            print("You have to take an uber home, which costs a lot of money")
        elif 0.3 <= self.drink_lvl < 0.08:
            self.fun_lvl -= 5
            print("You drive home, which is legal, but dangerous!")
        else:
            print("You drive home safely.")

        # prints results based upon your fun level
        print("My fun level was {}".format(self.fun_lvl))
        if 75 <= self.fun_lvl:
            print("That was one amazing night! Hope to do that again!")
        elif 50 <= self.fun_lvl < 75:
            print("That was an okay night. Hope things get better in the "
                  + "future!")
        elif 25 < self.fun_lvl < 50:
            print("That was a rough night.")
        else:
            print("That was not fun!")

class karaoke(person):

    def sing(self):
        """Allows the user to choose a song genre and then calls that method"""

        # chooses a song style and then calls that song method
        song_choice = input("Choose a song genre to sing "
                            + "('slow', 'pop', 'foreign', 'random'): ")
        if song_choice == "slow":
            karaoke.sing_slow(self)
        elif song_choice == "pop":
            karaoke.sing_pop(self)
        elif song_choice == "foreign":
            karaoke.sing_foreign(self)
        elif song_choice == "random":
            karaoke.sing_random(self)
        else:
            print("You can only karaoke to 'slow', 'pop', 'foreign', 'random',"
                  + "please try again.")

    def sing_slow(self):
        """Sings a slow song with different outcomes based on luck"""

        if random() <= self.luck:
            print("You brought the bar to tears! Fun +10")
            person.fun(self, 10)
        elif random() >= (1 - self.luck):
            print("You froze on stage from stage fright. Fun -10")
            person.fun(self, -10)
        else:
            print("You sang a slow song. Fun +5")
            person.fun(self, 5)

    def sing_pop(self):
        """Sings a pop song with different outcomes based on luck"""

        if random() <= self.luck:
            print("The bar goes wild chanting your name! Fun +10")
            person.fun(self, 10)
        elif random() >= (1 - self.luck):
            print("You sang in the wrong key. Fun -10")
            person.fun(self, -10)
        else:
            print("You sang a pop song. Fun +5")
            person.fun(self, 5)

    def sing_foreign(self):
        """Sings a foreign song with different outcomes based on luck"""

        if random() <= self.luck:
            print("The bar is confused but cheers you on! Fun +5")
            person.fun(self, 10)
        elif random() >= (1 - self.luck):
            print("You forgot the lyrics and looked awkward. Fun -10")
            person.fun(self, -10)
        else:
            print("You sang a foreign song. Fun +1")
            person.fun(self, 5)

    def sing_random(self):
        """Sings a random song with different outcomes based on luck"""

        if random() <= self.luck:
            print("The bar appreciates your creativity! Fun +10")
            person.fun(self, 10)
        elif random() >= (1 - self.luck):
            print("You lose self-confidence and run off stage. Fun -10")
            person.fun(self, -10)
        else:
            print("You sang a random song. Fun +5")
            person.fun(self, 5)

class bar_game(person):

    def play(self):
        """Allows the user to choose a bar game to play"""

        # chooses a bar game to play and then calls that bar game method
        play_game = input("Choose a game to play out of ('pool', 'darts', "
                          + "'shuffleboard', 'foosball', 'cornhole'): ")
        if play_game == "pool":
            bar_game.pool(self)
        elif play_game == "darts":
            bar_game.darts(self)
        elif play_game == "shuffleboard":
            bar_game.shuffleboard(self)
        elif play_game == "foosball":
            bar_game.foosball(self)
        elif play_game == "cornhole":
            bar_game.cornhole(self)
        else:
            print("You can only play the following bar games ('pool', "
                  + "'darts', 'shuffleboard', 'foosball', 'cornhole')")

    def pool(self):
        """Play a game of pool with different outcomes based on luck"""

        if random() <= self.luck:
            print("You made every ball in! Fun +10")
            person.fun(self, 10, 10)
        elif random() >= (1 - self.luck):
            print("You scratched on the 8 ball and lost the game. Fun -10")
            person.fun(self, -10)
        else:
            print("You enjoyed playing a good game. Fun +5")
            person.fun(self, 5, 10)

    def darts(self):
        """Play a game of darts with different outcomes based on luck"""

        if random() <= self.luck:
            print("You hit the bullseye several times and won! Fun +10")
            person.fun(self, 10, 15)
        elif random() >= (1 - self.luck):
            print("You missed the board, broke the darts, and had to pay "
                  + "for new ones. Fun -10")
            person.fun(self, -10, 10)
        else:
            print("You played well and improved your skill. Fun +5")
            person.fun(self, 5, 15)

    def shuffleboard(self):
        """Play a game of shuffleboard with different outcomes based on luck"""

        if random() <= self.luck:
            print("You score points in every round! Fun +10")
            person.fun(self, 10, 10)
        elif random() >= (1 - self.luck):
            print("You can't get your weights far enough on the table "
                  + "and lose badly. Fun -10")
            person.fun(self, -10, 10)
        else:
            print("You vow to get better at shuffleboard one day. Fun Level +5")
            person.fun(self, 5)

    def foosball(self):
        """Play a game of foosball with different outcomes based on luck"""

        if random() <= self.luck:
            print("You win by a shutout! Fun +10")
            person.fun(self, 10, 10)
        elif random() >= (1 - self.luck):
            print("You spin the players around, but can't seem to hit the "
                  + "ball. Fun -15")
            person.fun(self, -15, 10)
        else:
            print("You love foosball and enjoyed the game. Fun +5")
            person.fun(self, 5, 10)

    def cornhole(self):
        """Play a game of cornhole with different outcomes based on luck"""

        if random() <= self.luck:
            print("You make several sandbags into the hole! Fun +15")
            person.fun(self, 15, 15)
        elif random() >= (1 - self.luck):
            print("You hit more people than the hole and spilled several "
                  + "drinks. Fun -15")
            person.fun(self, -15, 15)
        else:
            print("You win some, you lose some. Fun +5")
            person.fun(self, 5, 15)

class drinking(person):

    def __init__(self):
        """Calls the name variable from the person class"""

        super().__init__(name)

    def drink(self):
        """Simulates going to a bar and ordering a drink. Users have several
        options to choose which can increase your BAC if there is alcohol
        present and increase your fun level. It takes 5 minutes to drink a
        drink due to waiting in line to order, the preparation of the drink,
        and then finishing your drink.
        """

        # Selecting a drink to order from
        print("The bar tender says 'Hi {}'".format(self.name))
        x = input("Would you like a "
                  + "('shot', 'beer', mixed drink', 'soda' or 'water'): ")

        if x == "shot" and self.drink_lvl < 0.27:
            print("You drank a shot! Fun +5, BAC +0.03")
            person.drink(self, 1)
            person.fun(self, 5, 5)
        elif x == "beer" and self.drink_lvl < 0.27:
            print("You drank a beer. Fun +5, BAC +0.03")
            person.drink(self, 1)
            person.fun(self, 5)
        elif x == "mixed drink" and self.drink_lvl < 0.24:
            print("You drank a mixed drink. Fun +5, BAC +0.06")
            person.drink(self, 2)
            person.fun(self, 5, 10)
        elif x == "soda":
            print("You drank soda and no one knows its non-alcoholic. Fun +5")
            person.drink(self, 0)
            person.fun(self, 5)
        elif x == "water":
            print("You drank water and are silently judged throughout the bar.")
            person.drink(self, 0)
            person.fun(self, 0)

        # separates those who will lose the game from alcohol poisoning
        elif (x == "beer" or x == "shot") and self.drink_lvl >= 0.27:
            person.drink(self, 1)
        elif x == "mixed drink" and self.drink_lvl >= 0.24:
            person.drink(self, 2)

        else:
            print("The bar tender says they do not understand what you wanted. "
                  + "Please type a ('shot', 'beer', mixed drink', 'soda' or "
                  + "'water') next time.")

class dancing(person):

    def dance(self):
        """Allows the user to choose a type of dance to perform"""

        # chooses a type of dance and then calls that dance method
        dance_choice = input("What kind of dance will you do ('jumping', "
                              + "'grinding', 'breakdance', 'two step', "
                              + "'shuffle'): ")
        if dance_choice == "jumping":
            dancing.jumping(self)
        elif dance_choice == "grinding":
            dancing.grinding(self)
        elif dance_choice == "breakdance":
            dancing.breakdance(self)
        elif dance_choice == "two step":
            dancing.two_step(self)
        elif dance_choice == "shuffle":
            dancing.shuffle(self)
        else:
            print("You only know how to do one of these dances ('jumping', "
                  + "'grinding', 'breakdance', 'two step', 'shuffle')")

    def jumping(self):
        """Jump to dance with different outcomes based on luck"""

        if random() <= self.luck:
            print("You impress the dance floor with your hops! Fun +5")
            person.fun(self, 5, 10)
        elif random() >= (1 - self.luck):
            print("You land funny and sprain your ankle. Fun -10")
            person.fun(self, -10)
        else:
            print("You get a good workout in while having fun. Fun +3")
            person.fun(self, 3, 10)

    def grinding(self):
        """Grind with people with different outcomes based on luck"""

        if random() <= self.luck:
            print("You grind on the nearest person and they kiss you "
                  + "passionately! Fun +20")
            person.fun(self, 20, 30)
        elif random() >= (1 - self.luck):
            print("You get slapped in the face several times from trying to "
                  + "grind on strangers and look foolish. Fun -20")
            person.fun(self, -20, 30)
        else:
            print("You got a phone number and only several slaps to the face. "
                  + "Fun +10")
            person.fun(self, 10, 30)

    def breakdance(self):
        """Breakdance with different outcomes based on luck"""

        if random() <= self.luck:
            print("Everyone takes snapchats of you for being awesome! Fun +15")
            person.fun(self, 15)
        elif random() >= (1 - self.luck):
            print("You accidentally kick someone and they punch you in the "
                  + "face. Fun -30")
            person.fun(self, -30)
        else:
            print("You sweat through your clothes, but now your muscles are "
                  + "swelling. Fun +5")
            person.fun(self, 5)

    def two_step(self):
        """Do the Texas Two-Steps with different outcomes based on luck"""

        if random() <= self.luck:
            print("You two-step like a Texan! Fun +10")
            person.fun(self, 10, 10)
        elif random() >= (1 - self.luck):
            print("The dance floor is too crowded for you to show your moves. "
                  + "Fun -5")
            person.fun(self, -5, 10)
        else:
            print("You dance with someone who gives you a free drink. Fun +5, "
                  + "BAC +0.03")
            person.drink(self, 1)
            person.fun(self, 5, 10)

    def shuffle(self):
        """Shuffle with different outcomes based on luck"""

        if random() <= self.luck:
            print("You look like a professional! Fun +5")
            person.fun(self, 5)
        elif random() >= (1 - self.luck):
            print("You break your shoes. Fun -15")
            person.fun(self, -15)
        else:
            print("You make new friends while shuffling. Fun Level +5")
            person.fun(self, 5, 10)

def menu():
    """This is the user menu that can start or exit the game"""

    # Until quit, the game can be played infinite amount of times
    main_menu = True

    while main_menu:
        print("--------Main Menu--------"
          + "\n Welcome to a night at Scooters")

        # try-except clause in case user enters a non-integer for input.
        try:
            choice = int(input("Please pick an option: \n"
                               + "1 - Play game \n"
                               + "2 - Quit: "))
            if choice == 1:
                game()

            # exits while loop if user decides to "quit" by inputting "2"
            elif choice == 2:
                main_menu = False
                print("Thank you for playing!")
                sys.exit()
            else:
                print("Error! Please enter 1 or 2")

        except ValueError:
                print("Error! Please enter 1 or 2")

def game():
    """Starts the game if called from the main menu"""

    # initialize the class instance
    name = str(input("Please enter your name "))
    x = person(name)

    print("""Welcome {}, to the game called 'A Night at Scooters'. The purpose
    of this game is to conduct activities throughout the night at a bar to
    hopefully have a great night out at Scooters! The game starts at 2000
    hours and continues until 0200 hours. Every activity that you decide to do
    will have a chance to increase or decrease your 'fun level'. Based on how
    high your fun level (0-100) is, will influence how happy you feel at the
    end of the night. Be careful with drinking too much alcohol though or you
    may end up in the hospital! You are now walking inside 'Scooters'
    """.format(x.name))

    # the game will not exceed 6 hours or 360 minutes since the game starts
    # at 2000 hours and ends at 0200 hours
    while x.time < 360:

        # try-except in case user inputs a non-integer number
        try:
            # choices available to call different classes and try to raise
            # fun leve or leave for the night
            choice = int(input("What would you like to do? \n"
                               + "1 - Karaoke \n"
                               + "2 - Play a bar game \n"
                               + "3 - Drink \n"
                               + "4 - Dance \n"
                               + "5 - Leave the bar: "))
            if choice == 1:
                karaoke.sing(x)
            elif choice == 2:
                bar_game.play(x)
            elif choice == 3:
                print("You want to drink. What would you like to drink?")
                drinking.drink(x)
            elif choice == 4:
                dancing.dance(x)
            elif choice == 5:
                print("You decide to go home")
                x.fun(0)
                x.time += 360
                continue
            else:
                print("Please enter a number between 1 and 5")

        except :
            print("Error! Please enter a number between 1 and 5")

    # if while loop is completed, go to credits
    else:
        x.end_night()
        credits()

def credits():
    """This is to give credits where credit is due."""

    print("--------Game over!-------- \n "
          + "Thank you for playing 'A Night at Scooters'. \n"
          + "This game was developed by Theodore Fong "
          + "for a project in the UC Berkeley MIDS W200 course "
          + "taught by Dr. Benoit.")

# starts the game
menu()
