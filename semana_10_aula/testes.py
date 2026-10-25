import unittest
import numeroromano as nr


class TestNumeroRomano(unittest.TestCase):

  def tearDown(self):
    print('Teste', self._testMethodName, 'finalizado.'); 

  def test_I(self):
    self.assertEqual(nr.converte('I'), 1, 'Erro na conversão de I para 1')

  def test_V(self):
    self.assertEqual(nr.converte('V'), 5, 'Erro na conversão de V para 5')

  def test_II(self):
    self.assertEqual(nr.converte('II'), 2, 'Erro na conversão de II para 2')

  def test_XXII(self):
    self.assertEqual(nr.converte('XXII'), 22, 'Erro na conversão de XXII para 22')

  def test_IX(self):
    self.assertEqual(nr.converte('IX'), 9, 'Erro na conversão de IX para 9')

  def test_XXIV(self):
    self.assertEqual(nr.converte('XXIV'), 24, 'Erro na conversão de XXIV para 24' )


if __name__ == '__main__':
  unittest.main()
