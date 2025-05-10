from psd_tools import PSDImage
from PIL import Image

# Charger le fichier PSD
psd = PSDImage.open('projet_credo.psd')

# Rasteriser le rendu entier du PSD en image PIL
composite = psd.composite()

nombre_exemplaires = input ("Entrer le nombre d'exemplaires à créer : ")

# verfier si l'entrée est un nombre entier et positif
try:
    nombre_exemplaires = int(nombre_exemplaires)
    if nombre_exemplaires <= 0:
        raise ValueError("Le nombre d'exemplaires doit être supérieur à zéro.")

except ValueError:
    print("Erreur : Veuillez entrer un nombre entier valide.")
    exit()
else:
    for i in range(nombre_exemplaires):
        nom_fichier = f"affiche_{i+1}.jpg"
        # Définir le chemin de destination
        chemin_de_sortie = f"/home/michel-nyembo/Images/{nom_fichier}"

        # Enregistrer l'image au format JPG
        composite.convert("RGB").save(chemin_de_sortie, "JPEG")

        print(f"Image enregistrée dans : {chemin_de_sortie}")
