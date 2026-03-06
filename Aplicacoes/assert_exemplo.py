#Assertion Condition
#True -> Program continue to run
#False -> Program stops and gives the assertion error

def operacao(a, b):
    
    resp = a/b
    print(resp)
    assert resp == 2.0, "Divisão não dá 2" 
    return resp


operacao(8,6)
operacao(55,11)
operacao(4,2)
operacao(7,2)
