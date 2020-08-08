# The type() function

name = "mpy"
fav_num = 18
tax_rate = 0.4

print(type(name))
print(type(fav_num))
print(type(tax_rate))

tax_rate = str(tax_rate)
print(type(tax_rate))

print(name.title() + " have " + str(fav_num) + " smartphone.")
print(name.title(), "have", fav_num, "smartphone.")