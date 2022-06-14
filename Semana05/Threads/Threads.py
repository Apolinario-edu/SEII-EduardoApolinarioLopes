#Codigo usando Threading 
#Threading permite subdividir um processo, acelerando sua execução.
#No exemplo em questão foram utilizadas as imagens disponibilizadas pelo autor 

#Codigo desenvolvido para testar threads 

import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    # for result in results:
    #     print(result)

# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')


###################################################################
#Usamos o codigo para fazer Download de imagens da rede de internet 

import requests
import time
import concurrent.futures

img_urls = [
   #URL das imagem desejadas 
]

t1 = time.perf_counter()


def download_image(img_url): #Passando o arguemento da imagem para download
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')
