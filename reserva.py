"""Modulo para gestionar reservas de habitaciones de hoteles."""

import csv


class Reserva:

    """ Clase reserva"""
    def __init__(self, clientes_file, hoteles_file, reservas_file):
        """ Incialización clase reserva"""
        self.clientes_file = clientes_file
        self.hoteles_file = hoteles_file
        self.reservas_file = reservas_file

    def realizar_reserva(self, cliente_id, hotel_id, habitacion):
        """ Metodo realizar reserva"""
        try:
            # Verificar si el cliente existe
            cliente_encontrado = False
            with open(self.clientes_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == cliente_id:
                        cliente_encontrado = True
                        break
            if not cliente_encontrado:
                print("Cliente no encontrado.")
                return False

            # Verificar si el hotel existe y la habitación está disponible
            hotel_encontrado = False
            habitacion_disponible = False
            with open(self.hoteles_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row[0].split(';')[0])
                    if row[0].split(';')[0] == hotel_id:
                        hotel_encontrado = True
                        habitacion_disponible = True
                        break
            if not hotel_encontrado:
                print("Hotel no encontrado.")
                return False
            if not habitacion_disponible:
                print("Habitación no disponible.")
                return False

            # Realizar la reserva
            with open(
              self.reservas_file, 'a', newline='', encoding='utf-8'
              ) as file:
                writer = csv.writer(file)
                writer.writerow([cliente_id, hotel_id, habitacion])
                print("Reserva realizada con éxito.")
                return True
        except FileNotFoundError:
            print("Error al realizar la reserva")
            return False

    def cancelar_reserva(self, cid, hid, hab):
        """ Método cancelar reserva"""
        try:
            # Leer las reservas existentes
            with open(self.reservas_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                reservas = list(reader)

            reserva_encontrada = False
            for res in reservas:
                if res[0] == cid and res[1] == hid and res[2] == hab:
                    reservas.remove(res)
                    reserva_encontrada = True

            if not reserva_encontrada:
                print("Reserva no encontrada.")
                return False

            # Escribir las reservas actualizadas en el archivo
            with open(
              self.reservas_file, 'w', newline='', encoding='utf-8'
              ) as file:
                writer = csv.writer(file)
                writer.writerows(reservas)

            print("Reserva cancelada con éxito.")
            return True

        except FileNotFoundError:
            print("Error al cancelar la reserva.")
            return False

    def consultar_reservas(self):
        """ Método para consultar las reservas"""
        try:
            with open(self.reservas_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                reservas = list(reader)
            return reservas

        except FileNotFoundError:
            print("No se pudo acceder al archivo de reservas.")
            return None
