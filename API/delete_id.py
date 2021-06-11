import urllib.parse
import urllib.request
import json

def Delete_id():
    url = 'http://localhost:5000/api/delete/clients/1080905060'
    values ={
        }

    params = json.dumps(values).encode('utf-8')
    print(params)
    req = urllib.request.Request(url,
                                data=params,
                                method='DELETE')
    response = urllib.request.urlopen(req)
    result = response.read()
    result = json.loads(result)

    # print (result)
    print("\nELIMINAR CLIENTE\n")
    for i in result:
        print (i,":",result[i])

    print("Cliente eliminado!")
