# Criar uma rede com segurança e privacidade utilizando a Rede Tor

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
