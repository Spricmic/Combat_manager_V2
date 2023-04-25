import csv


def get_monster_names():
    monster_names = []
    with open('monsters.csv', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            monster_names.append(row['name'])
    return monster_names


