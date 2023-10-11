print("a: Mars Bar")
print("b: Snickers")
print("c: Twix")
print("d: Bounty")

choice = input("Select an option (a, b, c, or d): ")

if choice == "a":
    print("Great choice! Here is your Mars Bar")
elif choice == "b":
    print("Great choice, Nutty! Here is your Snickers")
elif choice == "c":
    print("Great choice! Here is your Twix")
elif choice == "d":
    print("Poor choice, but who am I to judge! Here is your Bounty")
else:
    print("Invalid choice. Please select a valid option (a, b, c, or d).")