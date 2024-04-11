import time
import subprocess

def restart_proxies():
    proxies = [
        "sudo service tor restart",
        "sudo service squid restart",  # Exemplo de reiniciar o Squid Proxy (substitua pelo seu próprio proxy)
        "sudo service another_proxy restart"  # Exemplo de outro proxy na sua cadeia (substitua pelo seu próprio proxy)
    ]

    for proxy in proxies:
        try:
            subprocess.run(proxy, shell=True, check=True)
            print(f"Proxy reiniciado com sucesso: {proxy}")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao reiniciar o proxy {proxy}: {e}")

if __name__ == "__main__":
    restart_proxies()
