import threading
from serial_reader import SerialReader
import sys

def read_com_data(reader, data_store):
    """
    Reads data from the COM port in a separate thread.
    :param reader: Instance of SerialReader.
    :param data_store: Shared dictionary to store COM4 data.
    """
    while True:
        try:
            data = reader.read_line()
            if data:
                data_store["COM4"] = data
                print(f"[DEBUG] COM4 Data: {data}")
        except Exception as e:
            print(f"[ERROR] Failed to read COM4: {e}")

def read_scanner_data(data_store):
    """
    Reads data from the USB scanner in the main thread.
    :param data_store: Shared dictionary to store scanner data.
    """
    try:
        while True:
            print("[DEBUG] Waiting for scanner input...")
            scanner_data = input("Scanner Input: ").strip()  # Captures scanner input
            if scanner_data:
                data_store["Scanner"] = scanner_data
                print(f"[DEBUG] Scanner Data Updated: {scanner_data}")
    except KeyboardInterrupt:
        print("\n[DEBUG] Scanner input loop ended.")
    except Exception as e:
        print(f"[ERROR] Scanner input failed: {e}")

def main():
    # Configure serial port for COM4
    com4_port = 'COM4'  # Replace with your COM4 port
    baudrate = 9600

    # Shared data storage
    data_store = {"Scanner": None, "COM4": None}

    # Initialize SerialReader for COM4
    try:
        com4_reader = SerialReader(com4_port, baudrate)
        print("[DEBUG] SerialReader for COM4 initialized.")
    except Exception as e:
        print(f"[ERROR] COM4 initialization failed: {e}")
        sys.exit(1)

    # Start thread to read COM4 data
    com4_thread = threading.Thread(target=read_com_data, args=(com4_reader, data_store), daemon=True)
    com4_thread.start()

    print("[DEBUG] System initialized. Waiting for data...")

    try:
        # Read scanner data in the main thread
        read_scanner_data(data_store)
    except KeyboardInterrupt:
        print("\n[DEBUG] Program terminated by user.")
    finally:
        com4_reader.close()
        print("[DEBUG] Program ended.")

if __name__ == "__main__":
    main()
