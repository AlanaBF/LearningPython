import time

shipName = "Nastrama"
captain = "Wallace"
location = "Earth"
password = "Buttercups"

pAttempt = input("Enter your password: ")
while pAttempt != password:
    print ("Password is incorrect")
    pAttempt = input ("Enter the password: ")
print ("Password correct. Welcome to the " + shipName)   

print("")
print ("The spaceship " + shipName + " is currently visiting " + location + ". ")

choice = ""
while choice != "/exit":
    print ("What would you like to do, " + captain + "?")
    print ("")
    print ("a: Travel to another planet")
    print ("b: Fire cannons")
    print ("c: Open the airlock")
    print ("d: Self-destruct")
    print("/exit to exit")
    print ("")
    choice = input("Enter your choice: ")
    
    if choice == "a":
        destination = input("Where would you like to go? ")
        print ("Leaving " + location)
        print ("Travelling to " + destination)
        time.sleep(5)
        print ("Arrived at " + destination)
        location = destination
    elif choice == "b":
        print ("Firing Cannons")
        time.sleep(1)
        print("BANG!")    
        time.sleep(1)
    elif choice == "c":
        print ("Opening Airlock")
        time.sleep(3)
        print("Airlock Open!")    
        time.sleep(1)
    elif choice == "d":
        confirm = input ("Are you sure you want the ship to self destruct? (y/n)")
        if confirm == "y":
            print ("Ship will self destruct in")
            print ("3") 
            time.sleep(1)
            print ("2") 
            time.sleep(1)
            print ("1") 
            time.sleep(1)
            print ("Goodbye")
            print ("BOOM")
            choice = "/exit"
    elif choice == "/exit":
        print ("Good bye")        
    else: 
        print ("Invalid input. Please selct a,b,c or d.")    