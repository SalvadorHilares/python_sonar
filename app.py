class Usuario():
    def __init__(self, username):
        self.username = username

class CentroVacunacion():
    def __init__(self):
        self.total_personas = 22935533
        self.total_vacunados = 0

    def personas_vacunadas(self,personas):
        self.total_vacunados += personas