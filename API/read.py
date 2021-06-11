import urllib.request
import json

def Read():
    url = 'http://localhost:5000/api/get/clients'
    response = urllib.request.urlopen(url).read()
    print("Respuesta: \n")
    # print (response)
    # print("\n")

    listJson = json.loads(response)
    # print (listJson)
    # print("\n")

    print("LISTA DE CLIENTES\n")

    for i in listJson:
        # print (listJson[i])
        # print ("\n")
        for x in listJson[i]:
            for j in x:
                print(j,":",x[j])
            print ("\n")
    
