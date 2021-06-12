import urllib.parse
import urllib.request
import json

def Buy_product():
    url = 'http://localhost:5000/api/post/buy_products'
    values = {
        'cedula': "1127537146",
        'id': "0",
        'nombre': "leche",
        'cantidad': "3"
    }

    params = json.dumps(values).encode('utf-8')
    req = urllib.request.Request(url, data=params,
                                headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(req)
    result = response.read()

    # print (result)
    listJson = json.loads(result)
    # print (listJson)
    print("\nCOMPRAR PRODUCTOS\n")
    # print("\n")
    for i in listJson:
        # print (listJson[i])
        # print ("\n")
        for x in listJson[i]:
            print(x,":",listJson[i][x])

    print("\nCompra realizada!")