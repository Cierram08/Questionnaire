print("Welcome to my questionaire!")

playing = input("May I get to know you better? (yes/no) ")

if playing != 'yes' :
    print("As you wish. Goodbye!")
    quit()
else:
    print("Awesome! Let's play.")

behind = input("First, is someone behind you? ")
   
if behind == "no":
    print("Whew! That was close.")
else:
    print("Oh no! Let's try this another time! Bye!")
    quit()

name = input("Okay, what is your name? ")
print("Nice to meet you" + "," + " " + name + "!")

nickname = input("Do you have a nickname? (yes/no) ")
if nickname == "yes":
    friend = input("Please do share! ")
    print("That's a fun name! Mine is Cierra. Cie for short.")
    movie = input("Are you a Harry Potter fan" + "," + " " + friend + "? ")
    if movie == "yes":
        print("You have great taste! The movie is about to start actually.")
    else:
        print("Oh. One day we should chat about movies, but right now, HP is about to start!")
    goodbye = input("Can we chat later? (yes/no) ")
    if goodbye == "yes":
        print("Great! Talk soon!")
        quit()
    else:
        print("Well, I hope you change your mind. Have a great evening!")
        quit()

else:
    print("That's okay. I'll just call you " + name)
    movie = input("Are you a Harry Potter fan" + "," + " " + name + "? ")
    if movie == "yes":
        print("You have great taste! The movie is about to start actually.")
    else:
        print("Oh. One day we should chat about movies, but right now, HP is about to start!")
    goodbye = input("Can we chat later? (yes/no) ")
    if goodbye == "yes":
        print("Great! Talk soon!")
        quit()
    else:
        print("Well, I hope you change your mind. Have a great evening!")
        quit()
