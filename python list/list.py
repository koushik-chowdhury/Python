tea = ["Black","Green","Oolong","White"]
print(tea)
print(tea[0])
print(tea[-1])
print(tea[1:])
print(tea[::2])

tea[3] = "Herbal"
print(tea) 

tea[1:3] = ["Masala", "Ginger"]
print(tea)

print(tea[1:1])
tea[1:1] = ["test", "test"]
print(tea)