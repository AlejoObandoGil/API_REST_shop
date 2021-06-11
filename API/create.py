import urllib.parse
import urllib.request
import json

def Create():
    url = 'http://localhost:5000/api/post/clients'
    values ={
            'cedula': "123456789",
            'nombre': "Profe",
            'apellido': "Carlos",
            'email': "pepe@utp.edu.co",
            'telefono': "3101010",
            'direccion': "cra 20 #56-17"
            }

    params = json.dumps(values).encode('utf-8')
    req = urllib.request.Request(url, data=params,
                                headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(req)
    result = response.read()

    # print (result)
    listJson = json.loads(result)
    # print (listJson)
    print("\nCREAR CLIENTE\n")
    # print("\n")
    for i in listJson:
        # print (listJson[i])
        # print ("\n")
        for x in listJson[i]:
            print(x,":",listJson[i][x])

    print("\nCliente creado!")