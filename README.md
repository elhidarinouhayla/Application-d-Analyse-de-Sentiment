# Application-d'Analyse-de-Sentiment


## Objectif du projet 

L’objectif de ce projet est de créer un micro-service d’analyse de sentiment sécurisé, capable de recevoir des textes, de les envoyer à l’API Hugging Face pour évaluer leur sentiment avec le modèle nlptown/bert-base-multilingual-uncased-sentiment, et de retourner une note de 1 à 5. Le service doit être fiable, fonctionnel, protégé par JWT et facilement déployable grâce à Docker.


## Structure du projet
```
emotion_api/
│
├── app/                          
│   ├── sentiment.py     
│   ├── auth.py  
│   ├── shema.py   
│   ├── main.py           
│   └── config.py data/                     
│       ├── train/                
│       └── test/                
│
├── test/                        
│   └── test_predict.py
│
├── .env                         
├── gitignore                     
├── Dockerfile                                         
├── README.md                       
└── requirements.txt               

```


---

## Installation

1. Cloner le dépôt GitHub :  

```shell
    git https://github.com/elhidarinouhayla/Application-d-Analyse-de-Sentiment.git
    cd project
```

2. Créer un environnement virtuel :

 - Linux / Mac :
```shell
    python -m venv venv
    source venv/bin/activate
```
 - Windows :
```shell
    python -m venv venv
    venv\Scripts\activate
```

3. Installer les dépendances :

```shell
    pip install -r requirements.txt
```

4. Lancer l’API en mode développement :

```shell
    uvicorn main:app --reload
```

 - L’API sera accessible à l’adresse : http://127.0.0.1:8000

 - Documentation interactive Swagger : http://127.0.0.1:8000/docs

Astuce : Le paramètre --reload permet à l’API de se mettre à jour automatiquement à chaque modification du code, très pratique pour le développement.


## Configuration

```shell
HF_TOKEN=ton_token_huggingface
SECRET_KEY=une_clef_secrete
ALGORITHM=HS256
```

## Endpoint:/login

POST /login

Body :

```shell
{
  "username": "admin",
  "password": "abcd"
}
```

Reponse:

```shell
{
  "token": "xxxxx.yyyyy.zzzzz"
}
```

## Endpoit:/predict

POST/predict

Ce endpoit necessite:

 - un token valide
 - un texte dans le body

 Le backend appelle le modèle HuggingFace :

 ```shell
 nlptown/bert-base-multilingual-uncased-sentiment
```

### Classification des scores :

Score                          Sentiment
___________________________________________
 1,2                 |          negatif
_____________________|_____________________
  3                  |          neutre
_____________________|_____________________
 4,5                 |          positif
_____________________|____________________


## Tests Unitaires

Les tests vérifient que la route predict retourne :

   - 1 → negatif

   - 2 → negatif

   - 3 → neutre

   - 4 → positif

   - 5 → positif


### Commande pour lancer les tests :

```shell
pytest
```

## Dockerfile

Le Dockerfile permet de construire une image Docker pour le backend FastAPI.


Il fait les étapes suivantes :

  1. Utilise Python 3.11 slim comme base

  2. Définit le dossier de travail /app

  3. Copie le fichier requirements.txt et installe les dépendances Python

  4. Copie tout le code du backend dans l’image

  5. Expose le port 8000 pour l’API

  6. Lance le serveur Uvicorn à l’intérieur du conteneur

=> Cela permet de déployer facilement l’API sur n’importe quelle machine sans config supplémentaire

