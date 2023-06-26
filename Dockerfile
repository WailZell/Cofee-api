# Utilisez l'image de base Python pour Flask
FROM python:3.9-slim-buster

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installez les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiez les fichiers de l'application dans le conteneur
COPY . .

# Exposez le port sur lequel votre application Flask s'exécute
EXPOSE 5000

# Démarrez l'application Flask
CMD [ "python", "main.py" ]
