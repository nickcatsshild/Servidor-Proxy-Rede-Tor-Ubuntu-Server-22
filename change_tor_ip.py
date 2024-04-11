import time
import subprocess

def change_tor_ip():
    try:
        subprocess.run(['sudo', 'service', 'tor', 'restart'], check=True)
        print("Endereço IP do Tor alterado com sucesso.")
    except subprocess.CalledProcessError as e:
        print("Erro ao tentar reiniciar o Tor:", e)

if __name__ == "__main__":
    change_tor_ip()
