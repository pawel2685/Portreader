from serial_reader import SerialReader

def main():
    # Konfiguracja portu COM
    port = 'COM3'  # Zmień na odpowiedni port, jeśli potrzebne
    baudrate = 9600
    reader = None  # Zainicjuj reader jako None

    try:
        # Inicjalizacja SerialReader
        reader = SerialReader(port, baudrate)
        
        print("Czekam na dane (CTRL+C, aby zakończyć)...")
        while True:
            # Odczyt danych z portu
            data = reader.read_line()
            if data:
                print(f"Odebrane dane: {data}")
    except KeyboardInterrupt:
        print("\nProgram zakończony przez użytkownika.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    finally:
        # Sprawdź, czy reader został zainicjalizowany
        if reader and hasattr(reader, 'close'):
            reader.close()
        print("Program zakończony.")

if __name__ == "__main__":
    main()
