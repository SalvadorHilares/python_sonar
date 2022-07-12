import unittest
from app import Postas, Usuario,CentroVacunacion

class Tests(unittest.TestCase):

    user = Usuario('pepito')
    centro_vacunacion = CentroVacunacion()
    postas = Postas()

    def test_username(self):
        self.assertEqual(self.user.username,'pepito')

    def test_password(self):
        test_password=''.join(reversed(self.user.username))
        self.assertEqual(test_password,'otipep')

    def test_z_logout(self):
        self.user.username = ""
        self.assertEqual(self.user.username,"")

    def test_cant_postas(self):
        self.postas.total_centro_vacunacion = 10
        self.assertEqual(self.postas.total_centro_vacunacion,10)

    def test_total_vacunados_1(self):
        self.centro_vacunacion.personas_vacunadas_1(100000)
        self.centro_vacunacion.personas_vacunadas_1(150000)
        self.centro_vacunacion.personas_vacunadas_1(120000)
        self.assertEqual(self.centro_vacunacion.total_vacunados_1,370000, "Total vacunados 2")
    
    def test_vacunados_porcentaje_1(self):
        porcentaje_vacunados = (self.centro_vacunacion.total_vacunados_1/self.centro_vacunacion.total_personas)*100
        self.assertEqual(round(porcentaje_vacunados,2),1.61, "Porcentaje de vacunados 1")

    def test_alta_no(self):
        self.assertFalse(self.user.alta)
    
    def test_alta_si(self):
        self.user.alta = True
        self.assertTrue(self.user.alta)

    def test_total_vacunados_2(self):
        self.centro_vacunacion.personas_vacunadas_2(5000)
        self.centro_vacunacion.personas_vacunadas_2(7000)
        self.centro_vacunacion.personas_vacunadas_2(8000)
        self.assertEqual(self.centro_vacunacion.total_vacunados_2,20000, "Total vacunados 2")
    
    def test_vacunados_porcentaje_2(self):
        self.assertTrue(self.centro_vacunacion.total_vacunados_1>=self.centro_vacunacion.total_vacunados_2)
        porcentaje_vacunados = (self.centro_vacunacion.total_vacunados_2/self.centro_vacunacion.total_personas)*100
        self.assertEqual(round(porcentaje_vacunados,2),0.09,"Porcentaje de vacunados 2")
    
    def test_vacunados_senior(self):
        self.assertEqual(self.centro_vacunacion.porc_personas(15),-1)
        self.assertEqual(round(self.centro_vacunacion.porc_personas(20),2),0.08)
        self.assertEqual(round(self.centro_vacunacion.porc_personas(82),2),0.77)
        self.assertEqual(round(self.centro_vacunacion.porc_personas(75),2),0.24)
        self.assertEqual(round(self.centro_vacunacion.porc_personas(65),2),0.23)
        self.assertEqual(round(self.centro_vacunacion.porc_personas(54),2),0.15)
        self.assertEqual(round(self.centro_vacunacion.porc_personas(43),2),0.12)
        self.assertEqual(round(self.centro_vacunacion.porc_personas(33),2),0.10)