from polynomials import Polynomial
import pytest

#Test para mostrar por pantalla
def test_print():

    p=Polynomial((2,1,3,0,4))

    assert str(p) == "4x^4 + 3x^2 + x + 2"

#Test para ver identidad
def test_equality():
    assert Polynomial((0,1))==Polynomial((0,1))

#Tests para comprobar la suma
@pytest.mark.parametrize(
    "a, b, sum",
    (((0,),(0,1),(0,1)),
     ((2,0,3),(1,2),(3,2,3)),
     ((4,2),(10,2,4),(14,4,4)))
)

def test_add(a, b, sum):
    assert Polynomial(a) + Polynomial(b) == Polynomial(sum)


def test_add_scalar():
    assert Polynomial((2,1))+3==Polynomial((5,1))

def test_reverse_add_scalar():
    assert 3 +Polynomial((2,1))==Polynomial((5,1))

def test_add_unknown():
    with pytest.raises(TypeError):
        Polynomial((1,))+ "frog"


#Tests para comprobar la resta
@pytest.mark.parametrize(
    "a, b, sub",
    (((0,),(0,1),(0,-1)),
     ((2,0,3),(1,2),(1,-2,3)),
     ((4,2),(10,2,4),(-6,0,-4)))
)

def test_sub(a,b,sub):
    assert Polynomial(a) - Polynomial(b) == Polynomial(sub)

def test_sub_scalar():
    assert Polynomial((3,1))-2==Polynomial((1,1))

def test_reverse_sub_scalar():
    assert 3 -Polynomial((2,1))==Polynomial((1,1))

#Tests para comprobar la multiplicacion
@pytest.mark.parametrize(
    "a, b, mul",
    (((2,0,3),(1,2),(2,4,3,6)),
     ((4,2),(10,2,4),(40,28,20,8)),
     ((4,0,2),(10,0,0,4),(40,0,20,16,0,8)))
)

def test_mul(a,b,mul):
    assert Polynomial(a)*Polynomial(b) == Polynomial(mul)

def test_mul_scalar():
    assert Polynomial((3,1))*2==Polynomial((6,2))

def test_reverse_mul_scalar():
    assert 3*Polynomial((2,1))==Polynomial((6,3))

#Tests para comprobar la potencia
@pytest.mark.parametrize(
    "a, b, pow",
    (((2,0,3),3,(8,0,36,0,54,0,27)),
     ((4,2),2,(16,16,4)),
     ((0,-1,2),5,(0,0,0,0,0,-1,10,-40,80,-80,32)))
)

def test_pow(a,b,pow):
    assert Polynomial(a)**b == Polynomial(pow)

#Test para comprobar la evaluacion
@pytest.mark.parametrize(
    "a, b, ev",
    (((2,0,3),3,29),
     ((4,2),2,8),
     ((0,-1,2),5,45))
)

def test_ev(a,b,ev):
    assert Polynomial(a)(b)==ev

#Test para comprobar derivada
@pytest.mark.parametrize(
    "a, dx",
    (((2,0,3),(0,6)),
     ((4,2),(2,)),
     ((1,-1,2,0,5),(-1,4,0,20)))
)

def test_dx(a,dx):
    assert Polynomial(a).dx()==Polynomial(dx)