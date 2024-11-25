from flask import Flask, jsonify
from serial_reader import SerialReader
import threading
import logging
import time

# Setup logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Flask app setup
app = Flask(__name__)

# Shared data storage
data_store = {"COM4": None, "COM1": None}
data_lock = threading.Lock()  # Lock for thread safety

# Read COM4 data
def read_com4_data():
    com4_port = 'COM4'
    baudrate = 9600
    try:
        com4_reader = SerialReader(com4_port, baudrate)
        logging.info(f"COM4 Reader initialized on port {com4_port}.")
        print(f"[INFO] COM4 Reader initialized on port {com4_port}.")
        while True:
            new_com4_data = com4_reader.read_line()
            if new_com4_data:
                with data_lock:
                    data_store["COM4"] = new_com4_data
                    logging.info(f"COM4 Data Updated: {new_com4_data}")
                    print(f"[COM4] Received: {new_com4_data}")
    except Exception as e:
        logging.error(f"COM4 Reader failed: {e}")
        print(f"[ERROR] COM4 Reader failed: {e}")

# Read COM1 data (Scanner)
def read_com1_data():
    com1_port = 'COM1'
    baudrate = 9600
    try:
        com1_reader = SerialReader(com1_port, baudrate)
        logging.info(f"COM1 Reader initialized on port {com1_port}.")
        print(f"[INFO] COM1 Reader initialized on port {com1_port}.")
        while True:
            new_com1_data = com1_reader.read_line()
            if new_com1_data:
                with data_lock:
                    data_store["COM1"] = new_com1_data
                    logging.info(f"COM1 (Scanner) Data Updated: {new_com1_data}")
                    print(f"[COM1] Scanner Received: {new_com1_data}")
    except Exception as e:
        logging.error(f"COM1 Reader failed: {e}")
        print(f"[ERROR] COM1 Reader failed: {e}")

# Define the /port endpoint for COM4
@app.route('/port', methods=['GET'])
def get_com4_data():
    with data_lock:
        com4_data = {"COM4": data_store["COM4"]}
        print(f"[API] /port served: {com4_data}")
        return jsonify(com4_data)

# Define the /scanner endpoint for COM1
@app.route('/scanner', methods=['GET'])
def get_com1_data():
    with data_lock:
        com1_data = {"COM1": data_store["COM1"]}
        print(f"[API] /scanner served: {com1_data}")
        return jsonify(com1_data)

if __name__ == '__main__':
    # Start threads for COM4 and COM1
    threading.Thread(target=read_com4_data, daemon=True).start()
    threading.Thread(target=read_com1_data, daemon=True).start()

    # Run the Flask app with Waitress
    logging.info("Starting server on http://127.0.0.1:8080")
    print("[INFO] Starting server on http://127.0.0.1:8080")
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)
