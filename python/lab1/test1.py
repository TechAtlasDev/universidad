import requests
import json
    
ip_user = input("Pon la IP que quieres buscar: ")
response = requests.get(f"http://ip-api.com/json/{ip_user}").json()

if response["status"] != 200:
    print ("Datos de la dirección IP obtenida!")
    data = response

    print (json.dumps(data, indent=4))

else:
    raise ("No se pudo obtener los datos como corresponde")
