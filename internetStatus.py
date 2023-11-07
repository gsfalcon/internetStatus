import speedtest
import time

def get_network_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert from bits to megabits
    upload_speed = st.upload() / 1_000_000  # Convert from bits to megabits
    return download_speed, upload_speed

while True:
    download_speed, upload_speed = get_network_speed()
    print(f"Velocidade de download: {download_speed:.2f} Mb/s")
    print(f"Velocidade de upload: {upload_speed:.2f} Mb/s")
    time.sleep(1)  # Atualiza a cada segundo