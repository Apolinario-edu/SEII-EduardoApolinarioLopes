#Loops and Iterations
#For Loops 

nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found!')
        break      #O laço para ao achar o comando break 
    print(num) 

for num in nums:
    if num == 3:
        print('Found!')
        continue     #O laço printa Found no lugar de 3   
    print(num)


for num in nums:
    for letter in 'abc': #Usando 2 laços para printar um numero acompanhando de uma letra 
        print(num, letter)

for i in range(10): #Printa uma sequencia range de 10 posições
    print(i)

for j in range(1, 11):
    print(j) 
    
# Loops While

x = 0
while x < 10: # While entra no loop enquanto a condição for valida ( Enquanto x < 10 ) 
    print(x)    #Atenção pois While permite facilmente entrar em Loop infinito 
    x += 1

x = 0
while x < 10: # While entra no loop enquanto a condição for valida ( Enquanto x < 10 ) 
    if x == 5:
        print('Cinco')
    print(x)    #Atenção pois While permite facilmente entrar em Loop infinito 
    x += 1
    
