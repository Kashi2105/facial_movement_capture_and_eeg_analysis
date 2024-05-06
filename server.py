import socket
import serial
# Server details (match with Blender script)
SERVER_ADDRESS = "localhost"
SERVER_PORT = 5000

SERIAL_PORT = "COM6"  # Replace with your Arduino's port name
BAUD_RATE = 9600
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
def handle_client(conn):
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Received message: {data}")
        if data[6:9]=="113":
            ser.write(b'turn_on_led\n')
        if data[6:9]=="300":
            ser.write(b'turn_off_led\n')
        print(f"Sent to Arduino: {data}")
        while True:
            if ser.in_waiting > 0:
                response = ser.readline().decode().strip()  # Read response from Arduino
                print("Response from Arduino:", response)
                break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((SERVER_ADDRESS, SERVER_PORT))
    sock.listen(1)
    print(f"Server listening on {SERVER_ADDRESS}:{SERVER_PORT}")

    while True:
        conn, addr = sock.accept()
        print(f"Connected by {addr}")
        handle_client(conn)
        conn.close()
