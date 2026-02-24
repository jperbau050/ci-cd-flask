import unittest
from src.app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        # Crea un cliente de prueba usando la aplicación Flask
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # Envía una solicitud GET a la ruta '/'
        result = self.app.get('/')
        
        # Verifica que la respuesta sea "Hello, World!"
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode(), "Hello, World!")

    def test_404(self):
        # Verifica que una ruta que no existe devuelva el error 404
        response = self.app.get('/ruta-inexistente')
        self.assertEqual(response.status_code, 404)

    def test_home_content_type(self):
        # Verifica que la respuesta sea de tipo texto/html
        response = self.app.get('/')
        self.assertIn('text/html', response.content_type)

if __name__ == "__main__":
    unittest.main()