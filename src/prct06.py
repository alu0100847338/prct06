#!/src/bin/python
PI = 3.14155926535897931159979634685441852
def aproximacion(n):
  if (n!=0):
    suma = 0
    for i in range(1,n+1):
      xi = (i - (1/2)) / float(n)
      f_xi = 4 / (1 + xi**2)
      b = i / float(n)
      a = b - (1 / float(n))
      suma = suma + f_xi
    pi = suma/n
    return pi
n = int(raw_input('Introduzca el numero de intervalos: '))
m = int(raw_input('Introduzca el numero de veces que quieres que se repita la funcion: '))
lista = []
print aproximacion(n)
for j in range(1,m+1):
  pi = aproximacion(j*m)
  lista = lista + [pi]
print lista
