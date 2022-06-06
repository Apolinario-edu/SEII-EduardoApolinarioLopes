import matplotlib.pyplot as plt #Importando matplot -Seção 1 e 2- 

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Definindo vetores - Seção 3 - 

y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#plt.scatter(x,y) # Primeiro Grafico - Seção 4 - 
#plt.show()

import numpy as np

x1 = np.arange(0,100,1) #Semelhança com matlab, criando array de 0 a 999 variando de 1 em 1

plt.plot(x1, x1**2) # Cria grafico pra cada um dos valores mostrando a
                    # evolução ^2
                    #o Segundo arqumento nos permite manipular qual a função
                    # será aplicada ao nosso grafico 
plt.show()
  
