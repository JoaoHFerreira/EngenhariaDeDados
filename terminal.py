path_exibido = "->%/"
path_atual = "/"
TERMINAL_MAP = {
    "path_atual": path_atual,
    "path_infos": {path_atual: list()}
}

while True:
    comando = input(path_exibido)

    if comando == "pwd":
        print(TERMINAL_MAP["path_atual"])

    
    if comando.split(" ")[0] == "mkdir":
        # nome do path que será criado
        nome_do_path = comando.split(" ")[1]
        
        # inserção do path na lista de arquivos do path corrente
        TERMINAL_MAP["path_infos"][path_atual].append(nome_do_path)


        # criação do novo path
        TERMINAL_MAP["path_infos"][nome_do_path] = list()



    if comando == "ls":
        # irá listar informações do path atual
        print(TERMINAL_MAP["path_infos"][path_atual])


    if comando.split(" ")[0] == "echo":
        pass


    print(TERMINAL_MAP)

    



        
        



# precisamos armazenar os estados, quais ?
# O path atual
# Quais arquivos existem
# O conteúdo dos arquivos
