#Servidor

import socket
import select

HEADER_LENGTH = 10

IP = "127.0.0.1" #Neste campo nos defineinos o IP que será usado na comunicação, nesse caso, Local Host  
PORT = 1234 #Aqui, e definida a porta de comunicação 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criando o socket e definindo como ipv4 e TCP

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Permitindo a reconexão 

server_socket.bind((IP, PORT)) #Precisamos informar ao Sistema que iremos usar o Local Host e porta.

server_socket.listen() #Usado para permitir novas conexões

sockets_list = [server_socket] #lista de sockets

clients = {} #Necessario criar uma lista vazia para os clientes conectados

print(f'Listening for connections on {IP}:{PORT}...')


def receive_message(client_socket): #Função que recebe as mensagens e depois distribui para os clientes conectados

    try:

        
        message_header = client_socket.recv(HEADER_LENGTH) #Tamanho da mensagem

        if not len(message_header): #Laço usado para fechar caso não receba a mensagem 
            return False

        message_length = int(message_header.decode('utf-8').strip())

        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except:
       
        return False #Algo esta errado. 


while True: #Aqui criamos um loop para receber e enviar as mensagens para todos os sockets clientes. 
    
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list) #Esse função retorna um subconjunto das lista de entrada com os sockets prontos

    for notified_socket in read_sockets:#Laço para fazer a iteração  do sockets com os dados a serem lidos
       
        if notified_socket == server_socket: #A nova coneção acontece apenas caso o socket notificado for o socket do servidor 
           
            client_socket, client_address = server_socket.accept() #Aceita uma nova conexão
            
            user = receive_message(client_socket)#Cliente entra com o nome
            
            if user is False:#Se a informação for falsa o cliente desconectou
                continue

            sockets_list.append(client_socket) #Adiciona o socket para select.select() list

            clients[client_socket] = user #Salva seu username e seu cabeçalho

            print('Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))

         
        else: #Acessado se o socket notificado não for um socket de servidor, e nesse caso, temos uma mensagem para ler
            
            message = receive_message(notified_socket) #recebe a mensagem
            
            if message is False: #verficiando se realmente existe uma mensage, pois caso o cliente se desconecte, a mensagem estará vazia
                print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))
                
                sockets_list.remove(notified_socket) #remove da lista de socket.socket()
                
                del clients[notified_socket] #remove da lista de usuarios
                continue

            user = clients[notified_socket] #supondo que não foi uma desconexão

            print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            
            for client_socket in clients: #transmitindo para todos os clientes
                
                if client_socket != notified_socket: 
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    
    for notified_socket in exception_sockets: #Laço para caso não seja necessário, lidar com problemas de sockets
        
        sockets_list.remove(notified_socket) #remove da lista socket.socket()
        
        del clients[notified_socket] #Remove da lista de usuarios 
