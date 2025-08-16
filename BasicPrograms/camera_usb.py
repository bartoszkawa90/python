import serial.tools.list_ports
import serial

def list_usb_ports():
    """
    Lists all connected USB ports.
    """
    ports = serial.tools.list_ports.comports()
    usb_ports = [port.device for port in ports if "USB" in port.description]
    return usb_ports

def monitor_usb_port(port_name):
    """
    Monitors a USB port for incoming data.
    """
    try:
        with serial.Serial(port_name, baudrate=9600, timeout=1) as ser:
            print(f"Listening on {port_name}...")
            while True:
                if ser.in_waiting > 0:
                    data = ser.readline().decode('utf-8').strip()
                    print(f"Data received on {port_name}: {data}")
    except Exception as e:
        print(f"Error accessing {port_name}: {e}")

if __name__ == "__main__":
    usb_ports = list_usb_ports()
    if not usb_ports:
        print("No USB ports found.")
    else:
        print(f"Found USB ports: {usb_ports}")
        for port in usb_ports:
            print(f"Monitoring port: {port}")
            monitor_usb_port(port)  # Monitor each port found
