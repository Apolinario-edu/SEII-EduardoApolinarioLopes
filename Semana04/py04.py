#Listas, Tuplas e Conjuntos

#list

courses = ['History', 'Math', 'Physics', 'CompSci'] # Criando uma lista
print(courses) #Printa a lista 
print(len(courses)) #mostra a quantidade de elementos na lista

print(courses[3]) #Printa  String 3 da lista.
print(courses[0:2]) #Printa uma parte da string selecionada entre []. Porem vale lembrar que a lista resultante da chama inicia na string 0 e termina na string 1.

#Adicionando itens na lista 

courses.append('Art') #Adc arte como ultima string da lista
print(courses) 
courses.insert(0, 'Art') # Esse comando adc o curso Art na possição zero.
print(courses)

#Adicionando uma lista, em uma lista. 

courses2 = ['Art', 'Education']

courses.insert(0, courses2)
print(courses) #Nesse caso temos uma entrada onde o primeiro item recebe toda lista contendo Art e Education. Caso quisemos fazer uma alteração apenas em uma das strings não seria possivel.
                # Por exemplo, se fossemos printar o primeiro elemento da lista o resultado sera [Art, Education]

                
courses.extend(courses) #Concatena cada instring de forma individual na lista
print(courses)

# Invertendo os itens da lista

courses.reverse()
print(courses)


courses.sort() #Ajusta a lista de forma alfabetica, tambem funciona para uma lista numerica.
print(courses)

courses.sort(reverse=True) # Ajusta a lista de forma decrescente
print(courses)          

# Ajustando a lista com comando sorted

sorted_courses = sorted(courses)
print(sorted_courses)   #Esse comando ajusta a lista de forma alfabetica sem que se altere a lista original

    
#Obtendo maximo e minimo da lista numerica

print(max(nums))
print(min(nums))
print(sum(nums)) #Retorna a soma de todos os elementos da lista

#Obtendo Indices dos elementos da lista

print(courses.index('Art'))
print('Art' in courses) #Retorna True or False se o elesmente está na lista





