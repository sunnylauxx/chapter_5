person = input ("Enter your name: ")

print(person,'Welcome to Pokemon World! When you catch one pokemon successfully, you will earn 5 credits. In room one, you can catch grass pokemons. when you had earned 20 credits in room one then you can go to room two and catch fire pokemons. Again, when you had earned 30 points in room two, then you can go to room three and catch all types of pokemons! Enjoy!' )


print(" welcome to room 1! You can catch grass pokemons now!")


Bulbasaur = input (" Do you want to catch Bulbasaur?")


if Bulbasaur == "yes":
    print(" ************ waiting for the result **************")
    print(" Congratulations! Bulbasaur is in your bag!")
    print(" YOU RECEIVED 5 CREDITS!")
    
else:
    print(" ************ waiting for the result **************")
    print(" Ok. Bulbasaur escapes...")
    

        
Tangela = input (" Do you want to catch Tangela?")

if Tangela == "yes":
       print(" ************ waiting for the result **************")
       print(" Congratulations! Tangela is in your bag!")
       print(" YOU RECEIVED 5 CREDITS!")
       if Bulbasaur == "yes":
            print(" YOUR TOTAL CREDIT IS 10 NOW!")
       
else:
    print(" ************ waiting for the result **************")
    print(" Ok. Bulbasaur escapes...")
    
    if Bulbasaur == "yes":
        question = input(" Do you want to know your total credit now?")
        print(" YOUR TOTAL CREDIT IS 5 NOW!")
    
        
    

