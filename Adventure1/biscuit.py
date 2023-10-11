has_biscuits = input("Do you have any biscuits? ")

if has_biscuits == "yes":
    print("They look delicious")
    will_share = input("Can I have one? ")
    if will_share == "yes":
        print("Thank you!")
    else:
        print("I guess computers can't eat biscuits anyway...")
else:
    print("I don't believe you!")