from numbers import Number #para comrpobar si algo es un numero

class Polynomial:
    #El primer método inicializa a polinomio, tomandose a si mismo y los coeficientes p=Polynomial((0,1,3))
    def __init__(self, coefs):

        self.coefficients =coefs #atributo coeficientes

    #Este metodo devuelve el grado del polinomio
    def degree(self):

        return len(self.coefficients)-1
    
    #Este metodo se usa para mostrar en pantalla la representacion de p:  print(p)
    def __str__(self):

        coefs = self.coefficients
        terms = []

        #Casos especiales para termino independiente y x sin potencia 1
        if coefs[0]: #Porque si es 0 da falso
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1]==1 else coefs[1]}x") #f format para el string

        terms += [f"{''if c == 1 else c}x**{d}"
                  for d, c in enumerate(coefs[2:], start =2) if c ] #enumerate toma el índice para d (start en 2) y el obejto para c

        return " + ".join(reversed(terms)) or "0" #si terms está vacío, la primera parte será falsa y devuelve la segunda
    
    #Necesitamos un método para identificar polinomios iguales
    def __eq__(self, other):

        return self.coefficients==other.coefficients
    
    #definimos ahora la suma de polinomios (añadimos el caso en el que other sea un escalar primero)
    def __add__(self,other):

        if isinstance(other, Polynomial):
            common=min(self.degree(),other.degree())+1 #numero de terminos en comun incluyendo al independiente
            coefs = tuple(a + b for a, b in zip(self.coefficients, other.coefficients)) #zip recorre ambas tuplas y para cuando una se acaba
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)
        
        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0]+other,)+self.coefficients[1:]) #la coma detrás de other es para hacerlo una tupla de long 1

        else:
            return NotImplemented    


    def __radd__(self,other): #metodo para sumar por la izquierda
        return self+other