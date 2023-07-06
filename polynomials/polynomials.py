class Polynomial:
    def __init__(self, coefs):
        self.coefficients =coefs

    def degree(self):

        return len(self.coefficients)-1
