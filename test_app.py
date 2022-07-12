import unittest
from app import CentroVacunacion
from app import Usuario

class Tests(unittest.TestCase):

    user = Usuario('pepito')
    centro_vacunacion = CentroVacunacion()

    def test_username(self):
        self.assertEqual(self.user.username,'pepito')

    def test_password(self):
        test_password=''.join(reversed(self.user.username))
        self.assertEqual(test_password,'otipep')
    
    def test_vacunados(self):
        self.centro_vacunacion.personas_vacunadas(1000)
        self.centro_vacunacion.personas_vacunadas(1500)
        self.centro_vacunacion.personas_vacunadas(1200)
        self.assertEqual(self.centro_vacunacion.total_vacunados,3700)