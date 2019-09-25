

vectorOne = [0,4,1,5,7]
numbers = []

for i in vectorOne:
    if i not in [1,2,0,4,4]:
        numbers.append(i)

print(len(vectorOne))

print("********** RECORRING NUMBERS **********")

for n in numbers:
    print(n)