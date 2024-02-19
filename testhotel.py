# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fPDyU4yTiXpGYTzJrmJ6WiKybWrUuWtk
"""

import unittest
import os
from hotel import HotelManager

class TestHotelManager(unittest.TestCase):
    def setUp(self):
        # Crea un archivo de prueba para las pruebas
        self.file_path = 'test_hoteles.csv'
        self.manager = HotelManager(self.file_path)

    def tearDown(self):
    # Elimina el archivo de prueba después de las pruebas
      if os.path.exists(self.file_path):
        os.remove(self.file_path)

    def test_crear_hotel(self):
        # Verifica que se pueda crear un hotel correctamente
        habitaciones = ["0", "0", "0"]
        self.manager.crear_hotel("1000", "Hotel Ejemplo", "Calle Ejemplo 123", habitaciones)
        hoteles = self.manager.consultar_hoteles()
        self.assertIn(["1000", "Hotel Ejemplo", "Calle Ejemplo 123", "0", "0", "0"], hoteles)

    def test_borrar_hotel(self):
        # Verifica que se pueda borrar un hotel correctamente
        habitaciones = ["0", "0", "0"]
        self.manager.crear_hotel("2000", "Hotel Ejemplo", "Calle Ejemplo 123", habitaciones)
        self.manager.borrar_hotel("2000")
        hoteles = self.manager.consultar_hoteles()
        self.assertNotIn(["1", "Hotel Ejemplo", "Calle Ejemplo 123", "0", "0", "0"], hoteles)

    def test_actualizar_hotel(self):
        # Verifica que se pueda actualizar un hotel correctamente
        habitaciones = ["0", "0", "0"]
        self.manager.crear_hotel("3000", "Hotel Ejemplo", "Calle Ejemplo 123", habitaciones)
        self.manager.actualizar_hotel("3000", "Nuevo Nombre", "Nueva Dirección")
        hoteles = self.manager.consultar_hoteles()
        self.assertIn(["3000", "Nuevo Nombre", "Nueva Dirección", "0", "0", "0\n"], hoteles)

    def test_reservar_habitacion(self):
        # Verifica que se pueda actualizar un hotel correctamente
        habitaciones = ["0", "0", "0"]
        self.manager.crear_hotel("4000", "Hotel Ejemplo", "Calle Ejemplo 123", habitaciones)
        self.manager.reserva_habitacion("4000", 1)
        hoteles = self.manager.consultar_hoteles()
        self.assertIn(["4000", "Hotel Ejemplo", "Calle Ejemplo 123", "1", "0", "0\n"], hoteles)

if __name__ == '__main__':
    unittest.main()