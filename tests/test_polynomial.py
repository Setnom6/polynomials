from polynomials import Polynomial
import pytest

def test_print():

    p=Polynomial((2,1,3,0,4))

    assert str(p) == "4x**4 + 3x**2 + x + 2"

def test_equality():
    assert Polynomial((0,1))==Polynomial((0,1))


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