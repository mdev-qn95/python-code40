# Challenge: Favorite Teacher Program

print("Welcome to the Favorite Teachers Program")

fav_teaches = []

# Get user input
fav_teaches.append(input("\nWho is your first favorite teacher: ").title())
fav_teaches.append(input("Who is your second favorite teacher: ").title())
fav_teaches.append(input("Who is your third favorite teacher: ").title())
fav_teaches.append(input("Who is your fourth favorite teacher: ").title())

# Summary of list
print("\nYour favorite teachers ranked are: " + str(fav_teaches))
print("Your favorite teachers alphabetically are: " + str(sorted(fav_teaches)))
print("Your favorite teachers in reverse alphabetical order are: " + str(sorted(fav_teaches, reverse=True)))
print("\nYour top two teachers are: " + fav_teaches[0] + " and " + fav_teaches[1] + ".")
print("Your next two favorite teachers are: " + fav_teaches[2] + " and " + fav_teaches[3] + ".")
print("Your last favorite teacher is: " + fav_teaches[-1] + ".")
print("You have a total of " +  str(len(fav_teaches)) + " favorite teachers.")

# Insert a new favorite teacher
fav_teaches.insert(0, input("\nOops, " + fav_teaches[0] + " is no longer your first favorite teacher. Who is your new FAVORITE teacher: ").title())


# Summary of list
print("\nYour favorite teachers ranked are: " + str(fav_teaches))
print("Your favorite teachers alphabetically are: " + str(sorted(fav_teaches)))
print("Your favorite teachers in reverse alphabetical order are: " + str(sorted(fav_teaches, reverse=True)))
print("\nYour top two teachers are: " + fav_teaches[0] + " and " + fav_teaches[1] + ".")
print("Your next two favorite teachers are: " + fav_teaches[2] + " and " + fav_teaches[3] + ".")
print("Your last favorite teacher is: " + fav_teaches[-1] + ".")
print("You have a total of " +  str(len(fav_teaches)) + " favorite teachers.")

# Remove a specific teacher
fav_teaches.remove(input("\nYou've decided you no longer like a teacher. Which teacher would you like to remove from your list: ").title())

# Summary of list
print("\nYour favorite teachers ranked are: " + str(fav_teaches))
print("Your favorite teachers alphabetically are: " + str(sorted(fav_teaches)))
print("Your favorite teachers in reverse alphabetical order are: " + str(sorted(fav_teaches, reverse=True)))
print("\nYour top two teachers are: " + fav_teaches[0] + " and " + fav_teaches[1] + ".")
print("Your next two favorite teachers are: " + fav_teaches[2] + " and " + fav_teaches[3] + ".")
print("Your last favorite teacher is: " + fav_teaches[-1] + ".")
print("You have a total of " +  str(len(fav_teaches)) + " favorite teachers.")