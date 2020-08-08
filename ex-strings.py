#Strings

print("Hello World!")

full_name = "   Mpy master"
print(full_name)
print(full_name.upper())
print(full_name.lower())
print(full_name.title())
print(full_name.strip())

print(full_name)
full_name = full_name.title().strip()
print(full_name)

full_name = "\tMpy\nmaster"
print(full_name)

first_name = "mpy"
last_name = "master"
full_name = first_name + " " + last_name
print(full_name)
print(full_name.title())
print(first_name.upper() + " " + last_name.upper())

print(4+2)
print("4" + "2")

message = "Hello. How do you feel today?"
print(message)
message = message.lower()
h_count = message.count("h")
print("Có " + str(h_count) + " ký tự h bên trong message trên.")
print("Có", h_count, "ký tự h bên trong message trên.")

