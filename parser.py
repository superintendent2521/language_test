# im going to go fucking insane


s = input()
parts = s.split(" ") # Space here splits it so i can do logic


print(parts)
num1 = int(parts[0]) # fucked up example of getting both ints?
num2 = int(parts[2])

if 'PLUS' in parts:
    output = num1 + num2
    print(output)
