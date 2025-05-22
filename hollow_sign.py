import json
import random

# Load encounters
with open('encounters.json') as file:
    data = json.load(file)

tick_count = 0
tick_marks = ""

# Reaction table (2d6)
reaction_table = {
    2: "Immediate Attack",
    3: "Immediate Attack",
    4: "Hostile",
    5: "Hostile",
    6: "Cautious/Threatening",
    7: "Cautious/Threatening",
    8: "Cautious/Threatening",
    9: "Neutral",
    10: "Neutral",
    11: "Amiable",
    12: "Amiable"
}

def roll_die(sides):
    return random.randint(1, sides )

def roll_2d6():
        return roll_die(6) + roll_die(6)

def get_reaction():
    roll = roll_2d6()
    result = reaction_table.get(roll, "Unclear")
    return roll, result
 
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

          # Log to file
          with open("encounter_log.txt", "a", encoding="utf-8", errors="ignore") as log:
               log.write(f"Tick {tick_count}: {encounter['name']} | "
                    f"{encounter.get('notes', 'No notes.')} | "
                    f"Distance: {distance}ft | "
                    f"Reaction: {reaction_roll} -> {reaction}\n")

     else:
        print("No encounter this tick.")


while True: 
     input("\nPress Enter to take a Dungeon Turn...")
     add_tick()