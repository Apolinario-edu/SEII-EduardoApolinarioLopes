# Manipulando Arrays 

import numpy as np #Bibliotecas necessárias 

import matplotlib.pyplot as plt

a1 = np.array([4,6,8,2])    # Criando os Arrays 
a2 = np.zeros(10)
a3 = np.ones(4)
a4 = np.random.random(10)
a5 = np.random.randn(10)
a6 = np.linspace(0, 10, 100)
a7 = np.arange(0, 10, 0.2)

a1*2


2*a1>10


1/a4 + a4

plt.plot(a6, a6**2) #Plotando graficos 
plt.show()
 
plt.hist(a4)
plt.show() #Plotando graficos 

