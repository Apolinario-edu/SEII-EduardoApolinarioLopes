#Indexação

a1 = np.array([2,4,6,8,10]) # Definindo array 

a1[2] #Solicitando a posição 2  

a1[2:] #Solicitando posição 2 em diante 

a1[:-2] #Solicitando as 3 primeiras posições 

a1[::2] # 

a1>3

a1[a1>3]

names = np.array(['Jim', 'Luke', 'Josh', 'Pete'])
first_letter_j = np.vectorize(lambda s: s[0])(names)=='J' #Função Lambda, solicitada uma string e nos entrega o primeiro caractere da string

names[first_letter_j]

a1%4

a1%4==0

a1[a1%4==0]
