israin = input("Is it raining?")




if israin == "yes":
    iscold = input("Is it cold")
    if iscold == "yes":
        print("take raincoat")
        temperature = int(input("what is the temperature"))
        if temperature < 40:
                   print("take a hat")
    else:
        print("take umbrella")
        
                   
   
print("Don't forget your key")
