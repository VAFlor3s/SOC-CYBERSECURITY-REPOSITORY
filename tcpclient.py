import socket

def start_client():
    # Crear un socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Obtener el nombre del host
    host = socket.gethostname()
    port = 12345
    # Conectarse al servidor
    client_socket.connect((host, port))
    # Enviar un mensaje al servidor
    message = 'Hola, servidor.'
    client_socket.send(message.encode('utf-8'))
    # Recibir una respuesta del servidor
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Mensaje del servidor: {data}")
    # Cerrar la conexión
    client_socket.send("Un placer realizar el primer handshake contigo".encode('utf-8'))
    client_socket.close()
if __name__ == "__main__":
    start_client()