import socket #importando o modulo para trabalho com socket
import time   #importando o modulo para trabalho com tempo
import sys    #importando o modulo sys

UDP_IP = "127.0.0.1"        #IP do servidor UDP, local host 
UDP_PORT = 5005             #porta do servidor
buf = 1024                  #tamanho do buffer 
file_name = sys.argv[1]     #O nome do arquivo é definido através da leitura via terminal


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #inicialização do socket
sock.sendto(file_name, (UDP_IP, UDP_PORT))              #enviando o nome do arquivo
print("Sending %s ..." % file_name)                     #printando o status de envio

f = open(file_name, "r") #abrindo o arquivo para leitura
data = f.read(buf)       #lendo e armazenando os dados lidos


while(data): #Laço usado para enviar os dados para o IP e as portas atribuidas.
    if(sock.sendto(data, (UDP_IP, UDP_PORT))): 
        data = f.read(buf)                     #f.read permite a leitura do arquivo linha por linha
        time.sleep(0.02)                       #delay especificado

sock.close() #finalizando conexão
f.close()    #fechando o arquivo
