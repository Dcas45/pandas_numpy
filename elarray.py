import numpy as np
lista=[1,2,3,4,5,6,7,8,9]
print(lista)
np.array(lista)
print(np.array(lista))
arr=np.array(lista)
print(type(arr))
matriz=[[1,2,3],[4,5,6],[7,8,9]]
matriz=np.array(matriz)
print(matriz)
print(arr)
print(arr[1])
print(arr[0]+arr[5])
print(matriz)
print(matriz[0])
print(matriz[1])
print(matriz[2])
#print(matriz[3]) Aqui sale error de syntasis
print(matriz)
print(matriz[0,2])
print(arr[:6])
print(arr[2:])
print(arr[:])
print(arr[::3])
print(arr[-1])
print(arr[-3:])
print(matriz)
print(matriz[1:])
print(matriz[1:,0:2])


