import socket #importando o modulo para trabalho com socket
import select #importando o modulo select


UDP_IP = "127.0.0.1" #IP do servidor UDP, Local Host. 
IN_PORT = 5005       #porta do servidor
timeout = 3          #Nesse caso determinamos um tempo limite para a solictação 


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Criando o servidor UDP (trabalho com socket)
sock.bind((UDP_IP, IN_PORT)) #associação(bind) do socket com  Local Host


while True: #Laço usado para receber e armazenar os dados do sender(Cliente) 
    data, addr = sock.recvfrom(1024) 
    if data:    #verifica se dados não nulos
        print("File name:", data)   #printa o nome do arquivo
        file_name = data.strip()    #remove espaços do nome do arquivo

    f = open(file_name, 'wb')       #cria um arquivo para ser escrito em binário

    while True: #Laço usado para setar o metodo select para multiplexar a entrada e saída. 
        ready = select.select([sock], [], [], timeout) 
        if ready[0]:
            data, addr = sock.recvfrom(1024)           #recebendo e armazenando os dados do Cliente
            f.write(data)                              #escreve os dados lidos no arquivo
        else:
            print("%s Finish!" % file_name)            #printa a escrita
            f.close()                                  #fechando o arquivo
            break                                      #saindo do laço
        
