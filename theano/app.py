# Ejemplo theano libreria
import theano
from theano import tensor
# declaramos 2 escalares de punto flotante
a = tensor.dscalar()
b = tensor.dscalar()
# creamos la exresion simbolica
c = a + b
# convertimos la expresion en un objeto llamable que toma a y b y computa c
f = theano.function([a,b], c)
result = f(1.5,2.5)
print("*** THE RESULT IS: " + str(result) + ". ***")