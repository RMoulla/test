# Utiliser une image de base avec Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt ./
COPY app.py ./
COPY data/churn_model_clean.pkl ./data/



# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port sur lequel Flask tourne
EXPOSE 5012

# Définir la commande de démarrage du conteneur
CMD ["python", "app.py"]