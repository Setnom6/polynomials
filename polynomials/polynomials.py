class Polynomial:
    def __init__(self, coefs):

        self.coefficients =coefs

    def degree(self):

        return len(self.coefficients)-1
    
    def __str__(self):

        coefs = self.coefficients
        terms = []

        if coefs[0]: #Porque si es 0 da falso
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1]==1 else coefs[1]}x") #f format para el string

        terms += [f"{''if c == 1 else c}x**{d}"
                  for d, c in enumerate(coefs[2:], start =2) if c ] #enumerate toma el índice para d (start en 2) y el obejto para c

        return " + ".join(reversed(terms)) or "0" #si terms está vacío, la primera parte será falsa y devuelve la segunda