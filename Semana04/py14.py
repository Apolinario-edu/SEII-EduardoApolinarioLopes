
import os

os.chdir('/path/to/files/')

print(os.getcwd()) #Conferindo se estamos no diretorio correto 
print(dir(os))


for f in os.listdir(): #Esta laço printa os arquivos 
    if f == '.DS_Store':
        continue

    file_name, file_ext = os.path.splitext(f)
    print(file_name)

    # print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))

    f_title = f_title.strip()  #Removendo os espaços 
    f_course = f_course.strip()
    # f_number = f_number.strip()

    print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))

    print('{}-{}{}'.format(f_number, f_title.strip(), file_ext.strip())) #Formando como deseajdo 

    new_name = '{}-{}{}'.format(file_num, file_title, file_ext)

    os.rename(fn, new_name)  # Permite renomear 

print(len(os.listdir())) #Printando os itens 
