import serial

class SerialReader:
    def __init__(self, port, baudrate=9600, timeout=1):
        """
        Initialize the serial port.
        :param port: COM port, e.g., 'COM4'.
        :param baudrate: Baud rate for data transmission.
        :param timeout: Time to wait for data (in seconds).
        """
        try:
            self.ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)
            print(f"Connected to port: {port}")
        except serial.SerialException as e:
            print(f"Failed to open port {port}: {e}")
            raise

    def read_line(self):
        """
        Read a single line of data from the serial port.
        :return: The received line as a string.
        """
        try:
            data = self.ser.readline().decode('utf-8').strip()
            return data
        except Exception as e:
            print(f"Error reading data: {e}")
            return None

    def close(self):
        """
        Close the serial port.
        """
        self.ser.close()
        print("Port closed.")
