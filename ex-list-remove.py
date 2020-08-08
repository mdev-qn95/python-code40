# Removing elements from a list

language = ["Python", "AI", "R", "Java","AI"]

print(language)
language.remove("Java")
print(language)
language.remove("AI")
print(language)
language.remove("AI")
print(language)

print("\n")

new_language = ["Python", "AI", "R", "Java","AI"]
print(new_language)
remove_language = new_language.pop()
print("Removing the language " + remove_language)
bad_language = new_language.pop(1)
print("A bad language is " + bad_language)

print("\n")

print(language)
del language[0]
print(language)

print("\n")

array_language = []
array_language.append(input("Your language: "))
array_language.append(input("One more: "))
array_language.append(input("One more: "))
print(array_language)