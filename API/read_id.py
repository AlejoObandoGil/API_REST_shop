import urllib.request
import json

def Read_id():
    url = 'http://localhost:5000/api/get/1127537146'
    response = urllib.request.urlopen(url).read()
    print("Respuesta: \n")
    # print (response)
    # print("\n")
    listJson = json.loads(response)
    # print (listJson)
    # print("\n")
    print("BUSCAR CLIENTE\n")
    for i in listJson:
        # print (listJson[i])
        # print ("\n")
        for x in listJson[i]:
            print(x,":",listJson[i][x])

    print("\nCliente encontrado!")