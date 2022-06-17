import socket #importando o modulo para trabalho com socket
import sys    #importando o modulo sys

TCP_IP = "127.0.0.1"    #IP do servidor TCP (Local Host)
FILE_PORT = 5005        #porta de arquivo
DATA_PORT = 5006        #porta de dados
buf = 1024              #tamanho do buffer
file_name = sys.argv[1] #Aqui é definido o nome do arquivo através da leitura via terminal


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #inicialização(instancia) do socket
    sock.connect((TCP_IP, FILE_PORT)) #conexao do socket com o Local host
    sock.send(file_name)              #enviando o nome do arquivo
    sock.close() #finalizando o socket instanciado


    print("Sending %s ..." % file_name) #printando o status do envio do socket


    f = open(file_name, "rb") #Abrindo o arquivo para que seja feita a leitura em binário
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #inicialização(instancia) do socket
    sock.connect((TCP_IP, DATA_PORT))   #realiza a conexão com o host
    data = f.read()                     #armazenando os dados lidos no arquivo
    sock.send(data)                     #enviando os dados presentes no arquivo
finally:
    sock.close()    #encerrando a conexão
    f.close()       #fechando o arquivo
