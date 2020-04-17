##teste les méthodes de la classe véhicule

def test_method1():
    v1=Vehicule("red","ferrarri","200000")
    if (v1.method1() == 'red') 
        return True
    else :
        return False
      
def test_method2():
  v1=Vehicule("red","ferrarri","200000")
    if (v1.method2() == 'ferrarri') and (v1.method3() == '200000'):
        return True
    else :
        return False
      
def test_method3():
  v1=Vehicule("red","ferrarri","200000")
    if (v1.method3() == '200000'):
        return True
    else :
        return False

      
##teste sur la classe voiture

def test_details():
  c1=Car('blue','Citroen','15000')
  c1.details(3,2)
  if (c1.get_width() == 2):
    return True
  else:
    return False
