import numpy as np
# cero dimensiones
scalar = np.array(42)
print(scalar)
print(scalar.ndim)
# una  dimension
vector=np.array([1,2,3])
print(vector)
print(vector.ndim)
# dos dimensiones
matriz=np.array([[1,2,3],[4,5,6]])
print(matriz)
print(matriz.ndim)
#mas de dos dimensiones
tensor=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(tensor)
print(tensor.ndim)

#agregar o eliminar dimensiones
vector2=np.array([1,2,3,4], ndmin=10)
print(vector2)
print(vector2.ndim)
#expandir 
expand=np.expand_dims(np.array([1,2,3,4]),axis=0)
print(expand)
print(expand.ndim)
# eliminar dimensiones que no estas usando
print(vector, vector.ndim)
vector_2=np.squeeze(vector)
print(vector_2, vector.ndim)
