#Executando um processo em paralelo com Multiprocessamento
#Codigo usado para demonstrar o uso de sistemas Multi processados 

import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    # for result in results:
    #     print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')


#################################################################
#Codigo usado para Multi processamento de imagens 

import time
import concurrent.futures
from PIL import Image, ImageFilter

img_names = [
	#nome dos arquivos imagens
]

t1 = time.perf_counter()

size = (1200, 1200) #Aqui contamos o tamanho da imagem (No caso do exemplo do video 1200 pixels) 


def process_image(img_name): #O nome precisa ser o argumento 
    img = Image.open(img_name) #Abrindo imagem 

    img = img.filter(ImageFilter.GaussianBlur(15)) #Process Image Filter 

    img.thumbnail(size)
    img.save(f'process/{img_name}') #Salvando imagem na pasta process 
    print(f'{img_name} was process...')


with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, img_names) #Passando a função e a lista de imagens 
					   #Usando miltiprocessamento para as imagens 	

t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')
