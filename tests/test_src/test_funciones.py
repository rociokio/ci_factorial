<<<<<<< HEAD
import unittest
from src.funciones import factorial

class TestFactorial(unittest.TestCase):

    def test_factorial_1_pasa(self):
        """El factorial de 1 debería ser 1, pero aún no está implementado"""
        self.assertEqual(factorial(1), 1)

    def test_tipo_pasa(self):
        """Si pasamos un string en vez de un número, debería fallar"""
        with self.assertRaises(TypeError):
            factorial("texto")

    def test_negativo_pasa(self):
        """El factorial de un número negativo no está definido, debería lanzar un ValueError"""
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_positivo_pasa(self):
        """El factorial de 5 debería ser 120, pero la función aún no está implementada"""
        self.assertEqual(factorial(5), 120)

if __name__ == '__main__':
    unittest.main()
=======
import unittest
from src.funciones import factorial

class TestFactorial(unittest.TestCase):

    def test_factorial_1_pasa(self):
        """El factorial de 1 debería ser 1, pero aún no está implementado"""
        self.assertEqual(factorial(1), 1)

    def test_tipo_pasa(self):
        """Si pasamos un string en vez de un número, debería fallar"""
        with self.assertRaises(TypeError):
            factorial("texto")

    def test_negativo_pasa(self):
        """El factorial de un número negativo no está definido, debería lanzar un ValueError"""
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_positivo_pasa(self):
        """El factorial de 5 debería ser 120, pero la función aún no está implementada"""
        self.assertEqual(factorial(5), 120)

if __name__ == '__main__':
    unittest.main()
>>>>>>> f22c6e39cf5e011672f13dc451ef8c8c03fce8ab
