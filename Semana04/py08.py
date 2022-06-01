#Functions



def hello_func():  # Criamos a função hello_func 
    print('Hello Function.')

hello_func()


def hello_func(saudacao,saudacao2):  # função permite a entrada de dois valores com o uso de .format 
    return '{} {} Usuario.'.format(saudacao,saudacao2)

print(hello_func('Bem','Vindo'))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name ='John', age = 22)
