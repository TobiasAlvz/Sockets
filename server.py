import socket

def main():
    # Configurações do servidor
    host = '127.0.0.1'
    port = 12345

    # Criação do socket TCP/IP
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Liga o socket ao endereço e porta especificados
    server_socket.bind((host, port))

    # Define o número máximo de conexões pendentes
    server_socket.listen(1)

    print("Aguardando conexão do cliente...")

    # Aceita a conexão do cliente
    client_socket, client_address = server_socket.accept()

    print("Cliente conectado:", client_address)

    # Palavra a ser adivinhada
    palavra = "python"
    palavra_oculta = "" * len(palavra)
    chances = 5

    # Envia as informações iniciais para o cliente
    clientsocket.send(f"{palavra_oculta} {chances}".encode())

    # Loop principal do jogo
    while True:
        # Recebe a letra enviada pelo cliente
        letra = client_socket.recv(1024).decode().lower()

        # Verifica se a letra está na palavra
        if letra in palavra:
            # Atualiza a palavra oculta com a letra
            palavra_oculta = "".join([letra if letra == letra_palavra else oculta_letra for letra, letra_palavra, oculta_letra in zip(palavra, palavra_oculta, "" * len(palavra))])
        else:
            # Decrementa as chances
            chances -= 1

        # Verifica se o jogo terminou
        if palavraoculta == palavra or chances == 0:
            break

        # Envia a palavra oculta e as chances restantes para o cliente
        clientsocket.send(f"{palavraoculta} {chances}".encode())

    # Envia a palavra correta para o cliente
    clientsocket.send(palavra.encode())

    # Fecha o socket do cliente
    client_socket.close()

    # Fecha o socket do servidor
    server_socket.close()

if __name == "__main":
    main()