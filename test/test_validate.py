import validate



def test_add():
    calc=validate.Calculator()
    output = calc.list_add([1,2,3])
    assert output == 6
 
def test_multiply():
    calc=validate.Calculator()
    output = calc.list_multiply([1,2,3])
    
    assert output == 6



def test_maximum():
    calc=validate.Calculator()
    output = calc.list_maximum([1,2,3])
    
    assert output == 3