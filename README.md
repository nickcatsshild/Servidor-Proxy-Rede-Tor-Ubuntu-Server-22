# Criar uma rede com segurança e privacidade utilizando a Rede Tor

O que vou precisar de material?
Simples você precisa de um computador simples instalar Ubuntu Server 22 - Maquina fisica
Maquina virtual, criando pelo seu virtualizador preferido.

Para configurar um servidor Ubuntu 22.04 como um proxy Tor para compartilhar a rede Tor para outras máquinas na sua rede interna, você pode seguir os passos abaixo:

    Instale o Tor:
    Certifique-se de que o Tor está instalado no seu servidor Ubuntu. Se não estiver instalado, você pode fazê-lo utilizando o gerenciador de pacotes apt: 

sudo apt update
sudo apt install tor

# Configure o Tor como um proxy SOCKS:

Edite o arquivo de configuração do Tor para permitir conexões de outras máquinas na sua rede. Abra o arquivo de configuração do Tor em um editor de texto:

bash

sudo nano /etc/tor/torrc

Adicione ou modifique as seguintes linhas para configurar o Tor como um proxy SOCKS:

bash

SOCKSPort 0.0.0.0:9050 # Permitir conexões de qualquer IP na porta 9050

Salve e feche o arquivo de configuração.

Reinicie o serviço Tor:
Depois de fazer alterações na configuração do Tor, reinicie o serviço para aplicar as alterações:

sudo systemctl restart tor

Configurar as máquinas clientes:
Nas máquinas da sua rede interna que você deseja que usem o proxy Tor, você precisará configurá-las para usar o proxy SOCKS. Isso pode ser feito nas configurações do sistema ou do navegador, dependendo de como as máquinas estão configuradas.

    No sistema Ubuntu, você pode configurar o proxy SOCKS globalmente editando o arquivo nano /etc/environment e adicionando a linha:

        http_proxy="socks5://<IP_do_servidor_Tor>:9050"
        https_proxy="socks5://<IP_do_servidor_Tor>:9050"

        Substitua <IP_do_servidor_Tor> pelo endereço IP do servidor Tor na sua rede interna.

    Teste a conexão:
    Depois de configurar o proxy Tor no servidor e nas máquinas clientes, você pode testar se as conexões estão passando pelo Tor corretamente. Você pode fazer isso visitando um site como check.torproject.org para verificar se você está navegando usando o Tor.

Certifique-se de que o servidor Tor e as máquinas clientes estejam configuradas corretamente para usar o proxy SOCKS. Além disso, lembre-se de que o uso do Tor pode impactar a velocidade da sua conexão devido à criptografia e ao roteamento através da rede Tor.

# Aumentando a segurança do sistema com alteração de IPS automaticamente

Como o  Tor não oferece uma opção direta para alterar seu endereço IP a cada 15 minutos. é depende do seu nivel se quiser colocar 10 minutos ok sem problemas, faça testes.
No entanto, você pode configurar uma solução alternativa para alcançar esse objetivo. Uma abordagem comum é reiniciar o Tor periodicamente para obter um novo circuito e, consequentemente, um novo endereço IP.

Aqui está um exemplo de como você pode fazer isso usando um script em Python e o agendador de tarefas cron no Linux:

    Crie um script Python:

    Crie um arquivo Python chamado, por exemplo, change_tor_ip.py e adicione o seguinte código:

    python

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

Este script reiniciará o serviço Tor, o que geralmente resultará em uma mudança no endereço IP atribuído pelo Tor.

Permita a execução do script sem senha:

Você pode querer permitir que o usuário atual execute o comando sudo service tor restart sem a necessidade de uma senha. Para fazer isso, você pode editar o arquivo /etc/sudoers usando o comando sudo visudo e adicionar a seguinte linha ao final do arquivo:

css

username ALL=(ALL) NOPASSWD: /usr/sbin/service tor restart

Substitua username pelo seu nome de usuário.

Agende a execução do script:

Agora, você pode agendar a execução deste script usando o cron. Abra o terminal e digite:

crontab -e

Adicione a seguinte linha ao final do arquivo:

bash

    */15 * * * * /usr/bin/python3 /caminho/para/seu/script/change_tor_ip.py

    Isso programará o script para ser executado a cada 15 minutos. Certifique-se de substituir /caminho/para/seu/script/change_tor_ip.py pelo caminho real do seu script Python.

    Salve e feche o arquivo.

Com esta configuração, o serviço Tor será reiniciado a cada 15 minutos, o que geralmente resultará em um novo endereço IP. Certifique-se de testar o script e a programação do cron para garantir que tudo funcione conforme o esperado.

# Outra forma de fazer a alteração de IPS na nossa rede segura é alterar a cadeia de Proxy

Se você deseja alterar o endereço IP de forma programada em uma cadeia de proxies (como o Tor junto com outros proxies), você pode usar uma abordagem semelhante, mas em vez de reiniciar apenas o serviço Tor, você precisará reiniciar todos os serviços de proxy na cadeia.

Aqui está um exemplo de como você pode modificar o script Python para reiniciar uma cadeia de proxies:

python

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

Neste exemplo:

    proxies é uma lista de comandos para reiniciar os serviços de proxy na sua cadeia.
    subprocess.run(proxy, shell=True, check=True) executa cada comando na lista proxies e verifica se ocorreu algum erro.

Você precisará substituir "sudo service squid restart" e "sudo service another_proxy restart" pelos comandos específicos para reiniciar os proxies que você está usando na sua cadeia.

Depois de criar e testar o script, você pode agendar sua execução com o cron, seguindo os mesmos passos descritos anteriormente. Certifique-se de testar o script e a programação do cron para garantir que tudo funcione conforme o esperado.

$$ Lembre-se use com sabedoria o conhecimento como disse o Homen Aranha se fosse fizer merda: "Isso não é problema meu"

