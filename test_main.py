import pytest

def test_1_add(num1,num2):
    return num1+num2

def test_2_sub(num1,num2):
    assert num1 >= 0 and num2 >=0, "Number is less than Zero"
    return num1-num2


print(test_1_add(2,3))
print(test_2_sub(-1,3))