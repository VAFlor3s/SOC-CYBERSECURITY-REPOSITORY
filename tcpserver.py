import socket

def start_server():
    # Crear un socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Obtener el nombre del host
    host = socket.gethostname()
    port = 12345
    
    # Vincular el socket al puerto
    server_socket.bind((host, port))
    
    # Poner el socket en modo de escucha
    server_socket.listen(5)
    
    print(f"Servidor escuchando en {host}:{port}")
    
    while True:
        # Establecer la conexión con el cliente
        client_socket, addr = server_socket.accept()
        print(f"Conexión establecida con {addr}")
        
        # Recibir datos del cliente
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Mensaje del cliente: {data}")
        
        # Enviar una respuesta al cliente
        response = 'Hola, cliente. Tu mensaje fue recibido.'
        client_socket.send(response.encode('utf-8'))


        data=client_socket.recv(1024).decode('utf-8')
        print(f'Mensaje del cliente:{data}')
        # Cerrar la conexión con el cliente
        client_socket.close()

if __name__ == "__main__":
    start_server()