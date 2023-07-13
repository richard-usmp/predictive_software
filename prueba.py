import requests
import json

r = requests.post('https://api-tesis-usmp.herokuapp.com/prophetv3', json={'mes': 1, 'ventas': 19})
json_texto = r.text
jsondecoded = json.loads(json_texto[1:len(json_texto)-2])#quitar corchetes inicio y final
prediccion_ventas = jsondecoded["yhat"]
print(prediccion_ventas)