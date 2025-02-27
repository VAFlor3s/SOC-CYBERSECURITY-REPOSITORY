
import socket
from datetime import datetime
import scapy as scapy

def escaner_puertos(ip, ports):
    state_port=[]
    for port in ports:
        packet = scapy.IP(dst=ip)/scapy.TCP(dport=port, flags='S')
        response=scapy.sr1(packet, timeout=1, verbose= False )

        if response is None:
            print(f"Puerto {port}: cerrado o filtrado ")
        elif response.haslayer(scapy.TCP) and response.getlayer(scapy.TCP).flags==0x12:
            state_port.append(port)
            print(f"PUERTO {port}: Abierto ")
            try:
                service= servicio(ip.port)
                print(f"Servicio: {service}")
            except:
                print("Servicio desconocido")
        else:
            print(f"Puerto {port} cerrado")
    return state_port
    
def servicio(ip, port):
    try:
        soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.settimeout(2)
        soc.connect(ip,port)
        service_name= socket.getservbyport(port)
        soc.close
        return service_name
    except:
        return "Desconocido"




def main():
    target_ip = input("Introduce la dirección IP del objetivo: ")
    ports = [22,21, 80, 443, 8080, 21, 3306, 3389]
    
    print(f"Escaneando la IP {target_ip} en busca de puertos abiertos...\n")
    open_ports = escaner_puertos(target_ip, ports)
    
    if open_ports:
        print("\nPuertos abiertos encontrados:", open_ports)
    else:
        print("\nNo se encontraron puertos abiertos")


if __name__ == "__main__":
    main()
