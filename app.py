class Postas():
    def __init__(self):
        self.total_centro_vacunacion = 0

class Usuario():
    def __init__(self, username):
        self.username = username
        self.alta = False

class CentroVacunacion():
    def __init__(self):
        self.total_personas = 22935533
        self.total_vacunados_1 = 0
        self.total_vacunados_2 = 0

    def personas_vacunadas_1(self,personas):
        self.total_vacunados_1 += personas
    
    def personas_vacunadas_2(self,personas):
        self.total_vacunados_2 += personas

    def porc_personas(self,anios):
        if anios >= 80:
            return (5000/647355)*100
        elif anios>=70 and anios<=79:
            return (3000/1271842)*100
        elif anios>=60 and anios<=69:
            return (5000/2221241)*100
        elif anios>=50 and anios<=59:
            return (5000/3277134)*100
        elif anios>=40 and anios<=49:
            return (5000/4183174)*100
        elif anios>=30 and anios<=39:
            return (5000/5031117)*100
        elif anios>=18 and anios<=29:
            return (5000/6303670)*100
        else:
            return -1