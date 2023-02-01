import speedtest
import os

st = speedtest.Speedtest()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_internet_info():
    clear_console()
    print("Informações sobre sua conexão à internet:")
    print("Nome da conexão: ", st.get_best_servers()["sponsor"])
    print("IP: ", st.get_servers()["host"])
    print("Geolocalização: ", st.get_servers()["name"])
    print("Velocidade de download: ", st.download() / 10**6, "Mbps")
    print("Velocidade de upload: ", st.upload() / 10**6, "Mbps")
    print("Quantidade de dados transferidos: ", st.results.bytes_received / 10**9, "GB")

print_internet_info()
