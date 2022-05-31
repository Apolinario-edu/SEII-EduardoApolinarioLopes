courses = ['History', 'Math', 'Physics', 'CompSci']

for course in courses: #Para cada curso na minha lista, printa esse curso. 
    print(course)

for index, course in enumerate(courses): #Printa cada valor com seu indice 
    print(index, course)

for index, course in enumerate(courses, start=1): #Printa cada valor com seu indice a partir de 1 
    print(index, course)

courses_str = '-'.join(courses)  #Separa a lista com o caractere <->.Podemos usar qualquer caractere
print(courses_str)

new_list = course_str.split('-') #Retorna a lista original 
print(new_list)          
    
#Mutavel e Imutavel. Listas são mutaveis e tuplas são imutaveis. Isso pq não conseguimos alterar tuplas e listas sim

# courses = ['History', 'Math', 'Physics', 'CompSci'] é uma lista
# courses = ('History', 'Math', 'Physics', 'CompSci') é um Tupla.

# A unica diferença é que não podemos modificar a tupla, porem podemos acessa-la e usar seu valores normalmente

 courses = {'History', 'Math', 'Physics', 'CompSci'} # é um Conjunto. Em conjuntos a ordem não importar, ao printar as posições sempre mudam, pq a ordem n importa

# São uteis para analisar se um item esta na lista

print('Math' in cs_courses) # Verifica se o item Math esta na lista

art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses)) #Este comando verifica quais os itens que existem em comum entre os dois conjuntos 
print(cs_courses.difference(art_courses)) # Mostra os cursos que estão no conjunto CS mas não estao no Art 
print(cs_courses.union(art_courses)) # Fz um conjunto união entre os cursos que existem entre CS e Art

lista = [] # Cria uma lista
lista = list() # Cria uma lista

tupla =() #Cria uma tupla
tupla = tuple() #Cria uma tupla 

conjunto = {} # Para conjuntos, essa não é uma instrução valida.  
conjunto = set() # Esse é o comando correto para criar conjuntos.  
