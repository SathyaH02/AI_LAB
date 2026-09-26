# LAB 1 - VACUUM CLEANER SIMPLE REFLEX

# A -> RIGHT -> B
# B -> DOWN -> D
# D -> LEFT -> C
# C -> UP -> A


# Taking room status from user
rooms = {}

for room in ["A", "B", "C", "D"]:

    status = input(f"Enter status of Room {room} (clean/dirty): ").lower()

    while status not in ["clean", "dirty"]:
        print("Please enter only 'clean' or 'dirty'.")
        status = input(f"Enter status of Room {room} (clean/dirty): ").lower()

    rooms[room] = status


# Taking starting position
position = input("Enter starting position of vacuum (A/B/C/D): ").upper()

while position not in ["A", "B", "C", "D"]:
    print("Invalid position.")
    position = input("Enter starting position of vacuum (A/B/C/D): ").upper()


# Function to move the vacuum
def move(position):

    if position == "A":
        return "B", "RIGHT"

    elif position == "B":
        return "D", "DOWN"

    elif position == "D":
        return "C", "LEFT"

    elif position == "C":
        return "A", "UP"


# Display current state
def display_state():
    print("Vacuum position:", position)


# Agent
while "dirty" in rooms.values():

    display_state()

    # Reflex rule:
    # If current room is dirty -> CLEAN
    if rooms[position] == "dirty":

        print("Action: CLEAN")
        rooms[position] = "clean"

    # If current room is clean -> MOVE
    else:

        position, direction = move(position)

        print("Action:", direction)


display_state()

print("\nAll rooms are clean!")