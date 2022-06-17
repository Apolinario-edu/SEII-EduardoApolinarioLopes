import socket   #importando modulo para trabalho com socket


TCP_IP = "127.0.0.1"    #IP do servidor TCP (Local Host) 
FILE_PORT = 5005        #porta arquivo
DATA_PORT = 5006        #porta dados
timeout = 3             #setado tempo para requisição e solicitação
buf = 1024              #tamanho do buffer


sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #inicialização(instancia) do socket dos arquivos
sock_f.bind((TCP_IP, FILE_PORT))    #associação(bind) do socket com  localhost
sock_f.listen(1)    #abertura(listen) para solicitação de conexões


sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #inicialização(instancia) do socket dos dados
sock_d.bind((TCP_IP, DATA_PORT))  #associação(bind) do socket com  localhost
sock_d.listen(1)    #abertura(listen) para solicitação de conexões


while True: #Laço realizar as atribuições necessárias 
    conn, addr = sock_f.accept()    #atribuicao da conn e do address ao aceitar a conexao com o client
    data = conn.recv(buf)           #armazena o nome do arquivo
    if data:                        #Laço criado para verificar caso o nome do arquivo seja nulo ou vazio
        print("File name:", data)   #Printa o nome do arquivo
        file_name = data.strip()    #usado para remover espaços do nome do arquivo

    f = open(file_name, 'wb') #Indexa o arquivo em f

    conn, addr = sock_d.accept() #Aqui com a conexão com o cliente realizada é atribuida a Conn e o Address 
    while True:
        data = conn.recv(buf) #Armazenando os dados 
        if not data:          #Extrutura usada para garantir que se os dados forem vazios saia do laço
            break
        f.write(data)         #Escrevendo dados no arquivo

    print("%s Finish!" % file_name) #Printa a finalização da escrita do arquivo
    f.close()                 #fechando o arquivo
