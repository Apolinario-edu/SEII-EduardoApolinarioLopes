#Exemplo real de passagem de items.
#Nesse caso estamos trabalhando com duas listas. CSV e HTML

import csv # Importando CSV 

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    next(csv_data) #Aqui não passamos pela primeira linha com dados que não queremos 

    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output) 

