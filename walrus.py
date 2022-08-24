(y := len('hello'))
print(y)

people = ["Ben", "Isaac", "Muna"]
if (n := len(people)) <= 3: print(n)


lines = []


def canAdd(max = 3):
    global lines
    if allowed := (count := len(lines)) < max:
        print(f"You can enter {max - count} more")
    return allowed


while canAdd():
    lines.append(l := input('Enter a line'))

print(f'You entered: {lines}')
