# Challenge: Basketball Roster Program

print("Welcome to the Basketball Program")

# Get user input and define our roster
roster = []
player = input("\nWho is your point gaurd: ").title()
roster.append(player)
player = input("Who is your shooting gaurd: ").title()
roster.append(player)
player = input("Who is your small forward: ").title()
roster.append(player)
player = input("Who is your power forward: ").title()
roster.append(player)
player = input("Who is your center: ").title()
roster.append(player)

# Display roster
print("\n\tYour starting 5 for the upcoming basketball season")
print("\t\tPoint Gaurd:\t\t" + roster[0])
print("\t\tShooting Gaurd:\t\t" + roster[1])
print("\t\tSmall Forward:\t\t" + roster[2])
print("\t\tPower Forward:\t\t" + roster[3])
print("\t\tCenter:\t\t\t" + roster[4])

# Remove an injured player
injured_player = roster.pop(2)
print("\nOh no, " + injured_player + " is injured.")

roster_length = len(roster)
print("Your roster only has " + str(roster_length) + " players.")

# Add a new player
new_player = input("Who will take " + injured_player + "'s spot: ").title()
roster.insert(2, new_player)

# Display roster
print("\n\tYour starting 5 for the upcoming basketball season")
print("\t\tPoint Gaurd:\t\t" + roster[0])
print("\t\tShooting Gaurd:\t\t" + roster[1])
print("\t\tSmall Forward:\t\t" + roster[2])
print("\t\tPower Forward:\t\t" + roster[3])
print("\t\tCenter:\t\t\t" + roster[4])

print("\nGood luck " + roster[2] + " you will do great!")
roster_length = len(roster)
print("Your roster now has " + str(roster_length) + " players.")