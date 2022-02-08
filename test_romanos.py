import unittest

from romanos import RomanError, arabigo_a_romano, romano_a_arabigo

class RomanosFuncionesTest(unittest.TestCase):
    def test_arabigo_a_romano_sin_restas(self):
        self.assertEqual(arabigo_a_romano(36), 'XXXVI')

    def test_arabigo_a_romano_con_restas(self):
        self.assertEqual(arabigo_a_romano(464), 'CDLXIV')

    def test_arabigo_a_romano_solo_admite_enteros(self):
        with self.assertRaises(TypeError):
            arabigo_a_romano(str)

    def test_arabigo_a_romano_solo_enteros_positivos(self):
        with self.assertRaises(ValueError):
            arabigo_a_romano(0)


class RomanosFuncionesAromanoTest(unittest.TestCase):
    def test_romano_a_arabigo_tres_repeticiones_OK(self):
        self.assertEqual(romano_a_arabigo('III'), 3)

    def test_romano_a_arabigo_cuatro_repeticiones_ERROR(self):
        with self.assertRaises(RomanError):
            romano_a_arabigo('IIII')