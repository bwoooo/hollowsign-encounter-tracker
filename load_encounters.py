import json #Brings in the JSON library to read .json files

#Open the encounters.json file
with open('encounters.json') as file:
    data = json.load(file) #Load the file contents into a Python dictionary

#Print all monsters with their CR and notes
print("Monsters:")

for monster in data['monsters']:    #Loop throough each monster in the list
    name = monster['name']          #Get the monster's name
    cr = monster['cr']              #Get the monster's challenge rating
    notes = monster.get('notes', 'No notes.')   #Get notes (or a default if missing)

    print(f" - {name} (CR {cr}) - {notes}")  #Nicely format and print the info