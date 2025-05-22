import json
import random

# Load encounters
with open('encounters.json') as file:
    data = json.load(file)

tick_count = 0
tick_marks = ""

# Reaction table (2d6)
reaction_table = {
    (2, 3): "Immediate Attack",
    (4, 5): "Hostile",
    (6, 7, 8): "Cautious/Threatening",
    (9, 10): "Neutral", 
    (11, 12): "Amiable"
}

def roll_die(sides):
    return random.randint(1, sides )

def roll_2d6():
        return roll_die(6) + roll_die(6)

def get_reaction():
    roll = roll_2d6()
    for key, result in reaction_table.items():
         if roll in key:
              return roll, result
         return roll, "Unclear"
 
def get_random_encounter():
     roll = roll_die(10) -1 # d10 -> index 0-9
     return roll + 1, data['encounters'][roll]

def add_tick():
     global tick_count, tick_marks
     tick_count += 1
     tick_marks += "|"

     print(f"\n💀 Tick {tick_count} - {tick_count * 10} minutes passed.")
     print(f"Ticks: {tick_marks}")

     if roll_die(8) == 1:
          print("\n 👣 Encounter Detected!")
          roll, encounter = get_random_encounter()
          distance = roll_2d6() * 10
          reaction_roll, reaction = get_reaction()

          print(f" - Rolled: {roll} on the encounter table")
          print(f" - Name: {encounter['name']}")
          print(f" - Notes: {encounter.get('notes', 'No notes.')}")
          print(f" - Distance: {distance} feet")
          print(f" - Reaction Roll: {reaction_roll} -> {reaction}")
     else:
        print("No encounter this tick.")

# Run the turn loop
for _ in range(10): # Change to however many ticks you want to simulate
     input("\nPress Enter to take a Dungeon Turn...")
     add_tick()