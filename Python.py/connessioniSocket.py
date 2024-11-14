import socket as so

SRV_ADDR = "" #se è vuoto utilizza tutte le interfacce, altrimenti quella di appartenenza dell'indirizzo ip, esempio se ho 192.168.50.100 su eth0 mi basterà mettere 192.168.50.100 con collegamento eth0
SRV_PORT = 4444

s = so.socket(so.AF_INET, so.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))  #doppia parentesi per tupla, bind legge solo un parametro address
s.listen(1)
print("Sto attendendo una connessione...")
ris = s.accept()
#connection = ris[0]
#address = ris[1]
connection, address = s.accept()
print("Ho stabilito una connessione con: ", address)
while True:
    connection.sendall(b"C: ")
    data = connection.recv(1024)  #1024 sono i caratteri che posso ricevere prima di mettere in pausa
    if not data: break
    connection.sendall(b"Ho ricevuto il messaggio! \n")
    print(data.decode('utf-8'))
connection.close() #se non la chiudo il sistema operativo mi terrà il bind riservato
