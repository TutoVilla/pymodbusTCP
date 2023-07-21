from pyModbusTCP.server import ModbusServer, DataBank
import threading
import time

# Modbus TCP server configuration
SERVER_HOST = "192.168.13.14"  # Server IP address
SERVER_PORT = 502  # Default Modbus port
SLAVE_ID = 10  # Slave ID

def update_registers(regval):
    # Predefined values for holding registers
    
    REG_VAL_LEN = len(regval)
    databank = DataBank(h_regs_size=REG_VAL_LEN)
    
    for i, value in enumerate(regval):
        databank.set_holding_registers(i, [value]) 
                        
    return databank

class Server_Functions():
    @classmethod
    def run_server_sent_data(cls, regval):
        
        server = ModbusServer(host=SERVER_HOST, port=SERVER_PORT, no_block=True, data_bank = update_registers(regval))
        # Update register values at the beginning
        def start_server():
            try:
                print(f"Starting Modbus TCP server at {SERVER_HOST}:{SERVER_PORT}...")
                server.start()
            except KeyboardInterrupt:
                print("Stopping Modbus TCP server...")
                server.stop()
        # Crear y ejecutar el hilo para el servidor
        server_thread = threading.Thread(target=start_server)
        server_thread.start()
        # Esperar 5 segundos
        time.sleep(5)
        # Detener el hilo del servidor después de 5 segundos
        server_thread.join(timeout=0)
        print("Stopping Modbus TCP server...")
        server.stop()
        # Esperar 5 segundos
        time.sleep(5)
        return True






#from pyModbusTCP.server import ModbusServer, DataBank
#
## Modbus TCP server configuration
#SERVER_HOST = "192.168.13.14"  # Server IP address
#SERVER_PORT = 502  # Default Modbus port
#SLAVE_ID = 10  # Slave ID
#
#def update_registers():
#    # Predefined values for holding registers
#    REGISTER_VALUES = [100, 20, 30]
#    databank = DataBank(h_regs_size=3)
#    
#    for i, value in enumerate(REGISTER_VALUES):
#        databank.set_holding_registers(i, [value]) 
#                        
#    return databank
#
#if __name__ == "__main__":
#    # Create the Modbus TCP server
#    
#    server = ModbusServer(host=SERVER_HOST, port=SERVER_PORT, no_block=True, data_bank = update_registers())
#
#    # Update register values at the beginning
#
#    try:
#        print(f"Starting Modbus TCP server at {SERVER_HOST}:{SERVER_PORT}...")
#        
#        server.start()
#
#    except KeyboardInterrupt:
#        print("Stopping Modbus TCP server...")
#        server.stop()
