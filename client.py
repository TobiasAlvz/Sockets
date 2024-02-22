import socket

def main():
    # Configurações do cliente
    host = '127.0.0.1'
    port = 12345

    # Criação do socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta o socket ao servidor
    client_socket.connect((host, port))

    # Loop principal do jogo
    while True:
        # Recebe a palavra oculta e as chances restantes do servidor
        data = client_socket.recv(1024).decode()

        # Verifica se o jogo terminou
        if len(data) == len("python") + 2:
            palavra_correta = data
            print("Fim do jogo. A palavra era:", palavra_correta)
            break

        # Extrai a palavra oculta e as chances restantes
        palavra_oculta, chances = data.split()
        print("Palavra:", palavra_oculta, "Chances restantes:", chances)

        # Pede ao jogador para adivinhar uma letra
        letra = input("Digite uma letra: ")

        # Envia a letra para o servidor
        client_socket.send(letra.encode())

    # Fecha o socket do cliente
    client_socket.close()

if __name__ == "__main__":
    main()