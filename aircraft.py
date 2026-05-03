# FREEZE CODE BEGIN
class Aircraft:
    def __init__(self, model, altitude=0):
        self.model = model
        self.altitude = altitude

    def climb(self, feet):
        self.altitude += feet

    def descend(self, feet):
        self.altitude -= feet
# FREEZE CODE END
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