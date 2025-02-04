import csv

class Card:
    def __init__(self, name, hp, attack, defense, place):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.place = place

    def __repr__(self):
        return f"{self.name} (HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}, Place: {self.place})"
    

def read_cards(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [field.strip().replace(" ", "_") for field in reader.fieldnames]
        cards = []
        totalRows = 0
        for row in reader:
            totalRows += 1
            name, hp, attack, defense, place = row['Name'], row['HP'], row['Attack'], row['Defense'], row['Number']
            cards.append(Card(name, int(hp), int(attack), int(defense), int(place)))
            if totalRows == 10:
                break
    return cards