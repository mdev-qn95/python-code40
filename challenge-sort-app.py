# Lists Challenge: Grade Sorter App

print("Welcome to the Grade Sorter App")

# Initazile list and get user input
grades = []
grade = int(input("What's your first grade (0-100): "))
grades.append(grade)
grade = int(input("What's your second grade (0-100): "))
grades.append(grade)
grade = int(input("What's your third grade (0-100): "))
grades.append(grade)
grade = int(input("What's your fourth grade (0-100): "))
grades.append(grade)

print("Your grades are: " + str(grades))

# Sort the list from highest tho lowest
grades.sort(reverse=True)
print("Your grades from highest to lowest are: " + str(grades))

# Removing the lowest two grades
print("The lowest two grades will now be dropped.")
remove_grades = grades.pop()
print("Removed grade: " + str(remove_grades))
remove_grades = grades.pop()
print("Removed grade: " + str(remove_grades))

# Recap remaining grades
print("Your remaining grades are: " + str(grades))
print("Nice work! Your height grade is " + str(grades[0]) + ".")