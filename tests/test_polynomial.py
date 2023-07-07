from polynomials import Polynomial

def test_print():

    p=Polynomial((2,1,3,0,4))

    assert str(p) == "4x**4 + 3x**2 + x + 2"