import unittest

class Usuario():
    def __init__(self, username):
        self.username = username

class centroVacunacion():
    def __init__(self):
        self.total_personas = 22935533
        self.total_vacunados = 0

    def personas_vacunadas(self,personas):
        self.total_vacunados += personas

class Tests(unittest.TestCase):

    user = Usuario('pepito')
    centro_vacunacion = centroVacunacion()

    def test_login(self):
        test_password=''.join(reversed(self.user.username))
        self.assertEqual(self.user.username,'pepito')
        self.assertEqual(test_password,'otipep')
    
    def test_vacunados(self):
        self.centro_vacunacion.personas_vacunadas(1000)
        self.centro_vacunacion.personas_vacunadas(1500)
        self.centro_vacunacion.personas_vacunadas(1200)
        self.assertEqual(self.centro_vacunacion.total_vacunados,3700)

if __name__ == '__main__':
    unittest.main()