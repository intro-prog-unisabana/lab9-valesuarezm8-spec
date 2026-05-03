from aircraft import Aircraft

model = input()
plane = Aircraft(model)

while True:
    command = input()

    if command == "X":
        break

    parts = command.split()
    action = parts[0]
    value = int(parts[1])

    if action == "A":
        plane.climb(value)
    elif action == "D":
        plane.descend(value)

print(f"Final altitude: {plane.altitude} feet")