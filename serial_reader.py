import serial

class SerialReader:
    def __init__(self, port, baudrate=9600, timeout=1):
        """
        Inicjalizacja portu szeregowego.
        :param port: Port COM, np. 'COM4'.
        :param baudrate: Prędkość transmisji danych.
        :param timeout: Czas oczekiwania na dane.
        """
        try:
            self.ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)
            print(f"Połączono z portem: {port}")
        except serial.SerialException as e:
            print(f"Nie udało się otworzyć portu {port}: {e}")
            raise

    def read_line(self):
        """
        Odczytaj jedną linię danych z portu szeregowego.
        :return: Odebrana linia jako string.
        """
        try:
            data = self.ser.readline().decode('utf-8').strip()
            return data
        except Exception as e:
            print(f"Błąd podczas odczytu danych: {e}")
            return None

    def close(self):
        """
        Zamknij port szeregowy.
        """
        self.ser.close()
        print("Port zamknięty.")
