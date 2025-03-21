import requests
import pywhatkit as kit
import os

# Variables
file_id = 'https://drive.google.com/drive/folders/17WJVNIqCsQzZz-mIhUYiLnbBgqfBvLWV'  # Remplacez par l'ID de votre fichier Google Drive
google_drive_url = f'https://drive.google.com/uc?id={file_id}'
phone_number = '+237656360317'  # Remplacez par votre numéro WhatsApp
status_message = 'Voici mon nouveau statut !'

# Télécharger le fichier depuis Google Drive
response = requests.get(google_drive_url)

# Sauvegarder le fichier localement
if response.status_code == 200:
    file_path = 'status_media.jpg'  # Changez l'extension en fonction de votre fichier
    with open(file_path, 'wb') as f:
        f.write(response.content)
    print('Fichier téléchargé avec succès.')

    # Publier le statut sur WhatsApp
    kit.sendwhats_image(phone_number, file_path, status_message)
    print('Statut publié avec succès !')

    # Optionnel : Supprimer le fichier après envoi
    os.remove(file_path)
else:
    print('Échec du téléchargement du fichier.')
