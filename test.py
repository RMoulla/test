import requests

# URL de l'API Flask (modifie l'URL selon ton environnement Codespaces)
API_URL = "http://127.0.0.1:5012/predict"

# Données de test
payload = {
    "Age": 35,
    "Account_Manager": 1,
    "Years": 5.2,
    "Num_Sites": 3
}

# Envoyer une requête POST à l'API
response = requests.post(API_URL, data=payload)

# Afficher la réponse JSON
if response.status_code == 200:
    print("Réponse de l'API :", response.json())
else:
    print("Erreur lors de la requête :", response.status_code, response.text)