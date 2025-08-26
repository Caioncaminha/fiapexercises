def somar(a,b):
     return a+b

def multiplicar(lista):
     resposta = 1
     for elemento in lista:
          resposta = resposta*elemento
     return resposta

def soma_dois_primeiros(lista):
     if len(lista) < 2:
          return 'valores insuficientes'
     return lista[0]+lista[1]

def palindromo(text):	    
    i = 0
    j = len(text) - 1
    while j >= 0:
        if text[i] != text[j]:
            return False
        i += 1
        j -= 1
    return True 

import unittest

class TestesChiques(unittest.TestCase):

    def test01_pares(self):
        self.assertEqual(palindromo("abba"), True)
        self.assertEqual(palindromo("abbaabba"), True)
        self.assertEqual(palindromo("abca"), False)

    def test02_impares(self):
        self.assertEqual(palindromo("aba"), True)
        self.assertEqual(palindromo("abx"), False)

    def test03_pequenos(self):
        self.assertEqual(palindromo("a"), True)
        self.assertEqual(palindromo(""),  True)

    def test01_somar(self):
        self.assertEqual(somar(1,2),3)
        self.assertEqual(somar(10,2),12)
    
    def test02a_multiplicar(self):
         self.assertEqual(multiplicar([1,2,3]),6)

    def test02b_multiplicar(self):
         self.assertEqual(multiplicar([9]),9)

    def test03a_soma_dois_primeiros(self):
         self.assertEqual(soma_dois_primeiros([9,10]),19)
         self.assertEqual(soma_dois_primeiros([1,2,3,4,5]),3)

    def test03b_soma_dois_primeiros(self):
         self.assertEqual(soma_dois_primeiros([9]),'valores insuficientes')
         self.assertEqual(soma_dois_primeiros([]) ,'valores insuficientes')




def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestesChiques)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()