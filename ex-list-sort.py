# Sorting Lists and the len() function

sports = ["baseball", "golf", "soccer", "Football"]
print(sports)
print(sorted(sports))
print(sorted(sports, reverse=True))

array_a = [1, 3, 2, 18, 5, 100]
print(array_a)
print(sorted(array_a))
print(sorted(array_a, reverse=True))

array_length = len(array_a)
print(array_length)
print(type(array_length))

remove_array = array_a.pop()
print("Remove array " + str(remove_array))
print(len(array_a))

print(sports)
sports.sort()
print(sports)

print(array_a)
array_a.sort(reverse=True)
print(array_a)

print(sports)
sports.reverse()
print(sports)