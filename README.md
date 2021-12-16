# Rimac MLE Challenge
Microservicio basado en aprendizaje automático para estimar la probabilidad de una enfermedad del corazón.

## Uso
La aplicación por defecto se ejecuta de manera local y en el puerto 8080. 

```shell
http://0.0.0.0:8080
```
Solo cuenta con una ruta, siendo esta donde se encuentra el microservicio.

- POST /predict-heart-disease

El formato para las consultas es JSON y tiene la siguiente estructura:

```json
{
    "age": 10,
    "sex": "M",
    "chestPainType": "ATA",
    "restingBP": 140,
    "cholesterol": 289,
    "fastingBS": 0,
    "restingECG": "Normal",
    "maxHR": 123,
    "exerciseAngina": "N",
    "oldpeak": 1.5,
    "sTSlope": "Flat"
}
```

Y la estructura para la respuesta es el siguiente:

```json
{
    "prob": 0
}
```


## Pruebas

Para probar su funcionalidad se puede hacer mediante los siguientes comandos:

```shell
git clone https://github.com/CarlosCupe/rimac-mle-challenge.git
cd rimac-mle-challenge/
pip3 install -r requirements.txt
python3 app.py
```

## Despliegue

En caso se desee hacer el despliegue en un servidor se debera correr los siguientes comandos:

```shell
export FLASK_APP=app.py
flask run -p 2000
```