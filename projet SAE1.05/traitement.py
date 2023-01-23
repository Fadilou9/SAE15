import csv

# Ouvrez le fichier texte en mode lecture
with open('extrait.txt', 'r') as file:
    # Lisez les lignes du fichier
    lines = file.readlines()

    # Traitement des données (par exemple, séparation des colonnes)
    data = []
    for line in lines:
        columns = line.strip().split(',')
        data.append(columns)

    # Ouvrez un fichier CSV en mode écriture
    with open('extrait.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Écrivez les données traitées dans le fichier CSV
        writer.writerows(data)