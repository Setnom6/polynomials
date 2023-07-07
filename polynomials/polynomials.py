from numbers import Number, Integral #para comrpobar si algo es un numero

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

        terms += [f"{''if c == 1 else c}x^{d}"
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
    
    #Metodos para restar

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            common=min(self.degree(),other.degree())+1 #numero de terminos en comun incluyendo al independiente
            coefs = tuple(a - b for a, b in zip(self.coefficients, other.coefficients)) #zip recorre ambas tuplas y para cuando una se acaba
            other_restados=tuple(map(lambda n: -n, other.coefficients)) #forma de hacer una funcion rapida que cambie el signo
            coefs += self.coefficients[common:] + other_restados[common:]

            return Polynomial(coefs)
        
        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0]-other,)+self.coefficients[1:]) #la coma detrás de other es para hacerlo una tupla de long 1

        else:
            return NotImplemented 
        
    def __rsub__(self,other): #al no ser simétrica hay que hacerla de nuevo
        if isinstance(other, Polynomial):
            common=min(self.degree(),other.degree())+1 #numero de terminos en comun incluyendo al independiente
            coefs = tuple(b - a for a, b in zip(self.coefficients, other.coefficients)) #zip recorre ambas tuplas y para cuando una se acaba
            self_restados=tuple(map(lambda n: -n, self.coefficients)) #forma de hacer una funcion rapida que cambie el signo
            coefs += other.coefficients[common:] + self_restados[common:]

            return Polynomial(coefs)
        
        elif isinstance(other, Number):
            return Polynomial((-self.coefficients[0]+other,)+self.coefficients[1:]) #la coma detrás de other es para hacerlo una tupla de long 1

        else:
            return NotImplemented 
        

    #Implementamos ahora la multiplicación

    def __mul__(self, other):

        if isinstance(other, Polynomial):
            deg_max=self.degree()+other.degree()
            coefs=tuple()
            for a in range(deg_max+1):
                suma=0
                for i in range(self.degree()+1):
                    for j in range(other.degree()+1):
                        if i+j==a:
                            suma=suma+self.coefficients[i]*other.coefficients[j] #definicion obtenida de Alg conm y comptqui
                coefs+=suma,

            return Polynomial(coefs)
        
        elif isinstance(other, Number):
            coefs=tuple()
            for a in range(self.degree()+1):
                coefs+=other*self.coefficients[a],
            return Polynomial(coefs) #la coma detrás de other es para hacerlo una tupla de long 1

        else:
            return NotImplemented 

    def __rmul__(self,other):
        return self*other
    

    #Exponenciacion por una potencia entera positiva
    def __pow__(self,other):
        if isinstance(other,Integral) and other>=0:
            power=Polynomial((1,))
            for i in range(other):
                power=power*self
            return power
        else:
            return NotImplemented
        
    #Evaluación del polinomio en un escalar
    def __call__(self, other):
        if isinstance(other,Number):
            evaluacion=0
            for i in range(self.degree()+1):
                evaluacion+=self.coefficients[i]*other**i    
            return evaluacion
        else:
            return NotImplemented
