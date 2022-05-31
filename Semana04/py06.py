#Condicionais e Booleanos

language = 'Java'

if language == 'Python': #Comando If onde, oque estiver dentro so é executado se a condição estiver correta. Na validaçao if so entre oque é verdadeiro. 
    print('Language is Python') 

elif language == 'Java': #O Comando elif é usado para quando precisamos de uma sequencia de comparaçao. 
    print('Language is Java')

else:
    print('No match') # É acessado apenas se nem uma das comparações forem verdadeiras.

# Operador and.
# Esse operador retorna True se ambos os valores forem True e reporta False se qualquer valor for False

user = 'Admin'
logger_in = True

if user == 'Admin' and logger_in: # Aqui se logger_in = False, sera executado o comando else 
    print('Admin Page')
else:
    print('Bad Creds') 

    
# Operador or retorna True caso apenas um dos valores forem True.

user = 'Admin'
logger_in = True

if user == 'Admin' or logger_in:  
    print('Admin Page')
else:
    print('Bad Creds')

# Operador not muda um True para um False ou vice versa 

user = 'Admin'
logger_in = False


if not logger_in:  # A validação if so entre se ela for verdeira. Nesse caso nós mudamos a variavel logger_in por not logger_in é como Not false.
                   #Entao o if entende o valor como not false que é = true 
    print('Please Log In')
else:
    print('Welcome')

# operador is. Verifica se o ID das variaveis são os mesmos. 


