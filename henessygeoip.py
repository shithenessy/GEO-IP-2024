import requests
import subprocess
import getpass
import os
from colorama import init, Fore, Style

#INCIAR COLORAMA XD
init(autoreset=True)

# Esto es la (api) que hace la funcion de dar informacion
def obtener_info_geoip(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"{Fore.RED}No se pudo obtener información de GeoIP para {ip}. Estado de la solicitud: {response.status_code}{Style.RESET_ALL}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error al conectar con la API de GeoIP: {e}{Style.RESET_ALL}")
        return None

# Función para imprimir el banner con colores y efectos visuales
def imprimir_banner():
    banner = f"""
{Fore.RED} ▄██████▄     ▄████████  ▄██████▄        ▄█     ▄███████▄ {Style.RESET_ALL}
{Fore.YELLOW} ███    ███   ███    ███ ███    ███      ███    ███    ███ {Style.RESET_ALL}
{Fore.GREEN} ███    █▀    ███    █▀  ███    ███      ███▌   ███    ███ {Style.RESET_ALL}
{Fore.CYAN} ▄███         ▄███▄▄▄     ███    ███      ███▌   ███    ███ {Style.RESET_ALL}
{Fore.BLUE} ▀▀███ ████▄  ▀▀███▀▀▀     ███    ███      ███▌ ▀█████████▀  {Style.RESET_ALL}
{Fore.MAGENTA} ███    ███   ███    █▄  ███    ███      ███    ███ {Style.RESET_ALL}
{Fore.WHITE} ███    ███   ███    ███ ███    ███      ███    ███ {Style.RESET_ALL}
{Fore.YELLOW} ████████▀    ██████████  ▀██████▀       █▀    ▄████▀  {Style.RESET_ALL}
{Fore.CYAN} Dev: rockyy & henessy {Style.RESET_ALL}
"""
    subprocess.run(['cls' if os.name == 'nt' else 'clear'], shell=True)  # Limpiar pantalla
    print(banner)

# Función para mostrar la información de GeoIP formateada
def mostrar_info_geoip(info_geoip):
    print(f"\n{Fore.GREEN}Información de GeoIP:{Style.RESET_ALL}")
    print(f"IP: {info_geoip['query']}")
    print(f"País: {info_geoip['country']}, {info_geoip['regionName']}")
    print(f"Ciudad: {info_geoip['city']}")
    print(f"ISP: {info_geoip['isp']}")
    print(f"Latitud/Longitud: {info_geoip['lat']}, {info_geoip['lon']}")

# Función principal para la interacción con el usuario
def main():
    # Autenticación requerida
    usuario = input(f"{Fore.YELLOW}Usuario: {Style.RESET_ALL}")
    password = getpass.getpass(f"{Fore.YELLOW}Password: {Style.RESET_ALL}")

    if usuario != "henessy" or password != "root@cnc":
        print(f"{Fore.RED}Credenciales incorrectas. Saliendo...{Style.RESET_ALL}")
        return

    # Imprimir el banner al inicio
    imprimir_banner()

    while True:
        # Solicitud de dominio o IP
        dominio = input(f"\n{Fore.YELLOW}INGRESA UN (DOMINIO/IP) o 'exit' para salir: {Style.RESET_ALL}")

        if dominio.lower() == 'exit':
            print(f"{Fore.YELLOW}Saliendo del programa...{Style.RESET_ALL}")
            break

        # Obtener información de GeoIP
        info_geoip = obtener_info_geoip(dominio)

        if info_geoip:
            # Mostrar resultados
            mostrar_info_geoip(info_geoip)
        else:
            print(f"{Fore.RED}No se pudo obtener información de GeoIP para '{dominio}'. Inténtalo de nuevo.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
