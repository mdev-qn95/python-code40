# Changing or adding elements to a list

language = ["Python", "AI", "Java"]
print(language)
print(language[1])
print(language[-1])

language[1] = "R"
print(language)

language.append("AI")
print(language)

new_languague = []
new_languague.append("Python")
new_languague.append("Java")
new_languague.append("AI")
print(new_languague)

print(new_languague[1])
new_languague.insert(1, "Angular")
print(new_languague[1])
print(new_languague)

new_languague.insert(2, "Kotlin")
print(new_languague)