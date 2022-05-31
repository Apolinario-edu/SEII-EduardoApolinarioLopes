#Dicionarios

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
# print(student['courses']) Printa o valor desejado.

# print(student.get('phone', 'Not Found')) #Procura pelo valor e escreve a mensagem caso não ache o valor

student['phone'] = '555-555'
student['name'] = 'Carla'

print(student) # Os comando acima me permitem alterar itens do Dicionario

student.update({'name': 'Jane', 'age': 26})
print(student) # Altera a lista nos parametros especificamos 
 
age = student.pop('age') #Esse exclui a informação de idade da lista porem armazena na variavel age
print(age)

print(len(stundent) #Printa a quantidade de chaves do Dicionario student

print(student.keys()) #Printa as chaves
print(student.values()) # printa o conteudo das chaves 
print(student.items()) #  printa as cahves e seus valores

for key, value in student.items(): #Loop para printa cada chave e seus valores 
      print(key, value) 
