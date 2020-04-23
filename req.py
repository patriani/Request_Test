import requests
import sys # biblioteca para limpar buffer
import os


def req(url):
    r = requests.get(url) # Efetua requisição ao site com o endereço especificado
    code = r.status_code # code recebe código de retorno referente ao acesso ao site - o tipo de retorno define o tipo da variável
    return code

def decod(code): # Traduz o código de retorno http em uma mensagem escrita ("string")
    if code == 522:
        print('Status: Conexão lenta - tente novamente')
    elif code == 200:
        print('Status: Site no ar')
    elif code == 301 or code == 302: # ambos indicam que o site foi movido - permanentemente ou não
        print('Status: Site existe em outra URL')
    elif code == 404:
        print('Status: Site não existe no servidor')
    elif code == 500:
        print('Status: Servidor não suporta a funcionalidade')
    else:
        print('código de conexão não encontrado')


def config(opArquivo):
           
    if opArquivo == "1":
        arquivo = open('C:\\Users\\patri\\Desktop\\Geral\\Projetos_Web\\Req\\listaURL.txt', 'a') # abre arquivo com append
        print ("dentro do if 1")
        url = input('URL: ')
        sys.stdout.flush()
        arquivo.write(url+"\n")
        arquivo.close() # fecha arquivo
    
    elif opArquivo == "2":
        excluir = input('insira a url a ser excluida: ')
        sys.stdout.flush()
        arquivo = open('C:\\Users\\patri\\Desktop\\Geral\\Projetos_Web\\Req\\listaURL.txt', 'r') # abrindo arquivo para leitura
        linhas = arquivo.readlines() # ' variável "linhas" recebe todas as linhas do arquivo
        arquivo.close() # fechando arquivo que foi aberto no modo "leitura"
        
        arquivo = open('C:\\Users\\patri\\Desktop\\Geral\\Projetos_Web\\Req\\listaURL.txt', 'w')# abrindo arquivo para escrita
        
        for linha in linhas: # escreve todas as linhas, menos a selecionada para ser removid/a
            if linha != excluir + "\n":
                arquivo.write(linha)
        arquivo.close()
    
    else:

        arquivo = open('C:\\Users\\patri\\Desktop\\Geral\\Projetos_Web\\Req\\listaURL.txt', 'w') # abre arquivo com append
        arquivo.close() # fecha arquivo

def ini():
    
    arquivo = open('C:\\Users\\patri\\Desktop\\Geral\\Projetos_Web\\Req\\listaURL.txt','r')
    linhas = arquivo.readlines()
    
    for linha in linhas:
        
        linha = linha.replace('\n','')
        code = req(linha) # code recebe código de retorno do acesso à url contida na var linha
        print("Resultado para url: " +linha+ " ")
        print(decod(code))
        print("\n")

def main():
    confirma = ''
    os.system('cls' if os.name == 'nt' else 'clear')
    while(confirma != "sair"):
        confirma = input('\n\n Iniciar Aplicação ? [s/config/sair]\n\n') # Captura interação com usuário  
        sys.stdout.flush()

        if confirma == 's':
            os.system('cls' if os.name == 'nt' else 'clear')
            ini()
        elif confirma == 'config':

            while(confirma != "s"):
                os.system('cls' if os.name == 'nt' else 'clear') 
                print("\nConfig:\n")
                opArquivo = input("1: Adicionar url\n2: Remover um item\n3: Remover todos os itens\n_")
                sys.stdout.flush() # limpa buffer
                config(opArquivo)
                confirma = input("\nSair da configuração ? [s/n]\n")

            confirma = ''
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nFechando Programa\n")
        

if __name__ == "__main__":
    main()
