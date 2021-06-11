import urllib.parse
import urllib.request
import json

def Update_id():
    url = 'http://localhost:5000/api/update/1127537146'
    values ={
            'cedula': "987654321",
            'nombre': "sarita",
            'apellido': "agudelito",
            'email': "sarita@utp.edu.co",
            'telefono': "3999910",
            'direccion': "cra 2 #99-01"
            }

    params = json.dumps(values).encode('utf-8')
    # print(params)
    req = urllib.request.Request(url,
                                data=params,
                                headers={'content-type': 'application/json'},
                                method='PUT')
    response = urllib.request.urlopen(req)
    result = response.read()

    # print (result)
    listJson = json.loads(result)
    # print (listJson)
    print("\nACTUALIZAR CLIENTE\n")

    for i in listJson:
        # print (listJson[i])
        # print ("\n")
        for x in listJson[i]:
            print(x,":",listJson[i][x])

    print("\nCliente actualizado!")        
