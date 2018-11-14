from django.test import TestCase
from todos.views import listar, agregar_todo
from api_todos import settings

class TestTodo(TestCase):
    def testListarTODO(self):
        #settings.configure()
        resp = listar()
        self.assertEqual(len(resp), 0, "Error en listarTODO")
    def testAgregarTODO(self):
        agregar_todo({"texto" : "Data de prueba"})
        resp = listar()
        self.assertEqual(len(resp), 1, "Error en listarTODO")
        

