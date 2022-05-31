message = 'Hello  World'

print(len(message)); # Printa a quantidade de caracteres na string. Espaços contam como caracteres

print(message[0]) # Mostra a posição zero da string   ( Assim como para qualquer posição desejada ) 
print(message[0: 5]) # Mostra as posições entre 0 e 5 ( Assim para qualquer intervalo desejado ) 

print(message.lower()) # string toda miniscula 
print(message.upper())  # string toda maiuscula

print(message.count('l')) # Conta a quantidade de L's na string
print(message.find('Hello')) # Procura por Hello na string retorna a posição onde a palavra está

message = message.replace('World','Universe') # Este comando faz com que a string world seja trocada pela string Universe

print(message)

# Contatenando Strings

name = 'Eduardo' 
name2 = ' Bem vindo'

message2 = name + name2 

print(message2)

message2 = '{}, {}. Welcome!'.format(name, name2) # Concatenando com o comando .formar 

print(message2)

message3 = f'{name}, {name2}' # Concatenando com .f 

print(message3)
