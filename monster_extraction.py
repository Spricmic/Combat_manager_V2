import requests
import csv

attributes = ['name', 'size', 'pros', 'type', 'armor_class', 'hit_points', 'speed', 'strength', 'dexterity',
              'constitution', 'intelligence', 'wisdom', 'charisma', 'strength_save', 'dexterity_save',
              'constitution_save', 'intelligence_save', 'wisdom_save', 'charisma_save', 'skills',
              'damage_vulnerabilities', 'damage_resistances', 'damage_immunities', 'condition_immunities',
              'senses', 'challenge_rating', 'actions', 'reactions', 'legendary_desc', 'legendary_actions',
              'special_abilities', 'spell_list']

# Create a list to store the monster data
monsters = []

# Make a GET request to the Open5e API's monsters endpoint
url = 'https://api.open5e.com/monsters/'
response = requests.get(url)

# Check that the request was successful
if response.status_code == 200:
    # Extract the first page of monster data
    data = response.json()
    monsters.extend(data['results'])

    # Iterate over the pages of monster data
    while data['next']:
        # Make a GET request to the next page of monster data
        url = data['next']
        response = requests.get(url)

        # Check that the request was successful
        if response.status_code == 200:
            # Extract the monster data from the response
            data = response.json()
            monsters.extend(data['results'])
        else:
            print(f'Error: Could not retrieve monster data from {url}')
            break

    # Write the monster data to a file
    with open('monsters.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(attributes)
        for monster in monsters:
            row = []
            if '"' in monster['name']:
                # Remove the substring using the replace() method
                monster['name'] = monster['name'].replace('"', '')
            for attribute in attributes:
                if attribute in monster:
                    row.append(monster[attribute])
                else:
                    row.append('N/A')
            writer.writerow(row)

    print('Monster data successfully written to monsters.csv')
else:
    print('Error: Could not retrieve monster data from the API.')
