again = "yes"
while again == "yes":
    praiseType = input("Select a type of praise \n a:personality\n b:appearance \n c:intelligence \n")
    if praiseType == "a":
        print ("You are an interesting person")
    elif praiseType == "b":
        print ("You are smart")
    elif praiseType == "c":
        print ("You look good")        
    else: print ("That was not an option!")
    again = input ("Would you like more praise?")        
