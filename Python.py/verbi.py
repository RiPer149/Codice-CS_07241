import http.client

host = input("Inserisci host/ip del sistema target: ")
port = input("Inserisci la porta del sistema target (default: 80): ")
path = input(" Inserisci il percorso (default:'/'): ")

if(port==""): port = 80
if(path==""): path = '/'

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('OPTIONS', path)
    response = connection.getresponse()
    if(response.status == 200 and response.status <= 299 and response.getheader("Allow") != None):
        print("I metodi abilitati sono: ", response.getheader("Allow"))
    else:
        print("Usa un metodo alternativo per determinare i verbi\n", response.status, response.getheader)

    connection.close()
except ConnectionError:
    print("Connessione fallita", ConnectionError.strerror)
