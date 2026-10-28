import os

LIMITE_CARACTERES = 50
MANTER_CARACTERES = 45


def renomear_arquivos():

    pasta_atual = os.path.dirname(os.path.abspath(__file__))


    if os.name == 'nt' and not pasta_atual.startswith('\\\\?\\'):
        diretorio_longo = '\\\\?\\' + pasta_atual
    else:
        diretorio_longo = pasta_atual

    print(f"Analisando pasta: {pasta_atual}\n")

    contador = 0
    total_lidos = 0

    try:

        lista_arquivos = os.listdir(diretorio_longo)
    except Exception as e:
        print(f"[ERRO] Não foi possível ler a pasta: {e}")
        return


    for nome_arquivo in lista_arquivos:

        if nome_arquivo == os.path.basename(__file__):
            continue


        caminho_completo = os.path.join(diretorio_longo, nome_arquivo)


        if os.path.isfile(caminho_completo):
            total_lidos += 1
            tamanho = len(nome_arquivo)
            print(f"[#{tamanho} chars] {nome_arquivo}")


            if tamanho > LIMITE_CARACTERES:

                nome_base, extensao = os.path.splitext(nome_arquivo)


                novo_nome_base = nome_base[:MANTER_CARACTERES]

                novo_nome = f"{novo_nome_base}{extensao}"


                caminho_novo = os.path.join(diretorio_longo, novo_nome)
                contador_duplicados = 1


                while os.path.exists(caminho_novo):
                    novo_nome = f"{novo_nome_base}_{contador_duplicados}{extensao}"
                    caminho_novo = os.path.join(diretorio_longo, novo_nome)
                    contador_duplicados += 1


                try:
                    os.rename(caminho_completo, caminho_novo)
                    print(f"   -> [SUCESSO] Renomeado para: {novo_nome}")
                    contador += 1
                except Exception as e:

                    print(f"   -> [ERRO] Falha ao renomear: {e}")


    print(f"\n--- Processo Concluído ---")
    print(f"Total de ficheiros analisados: {total_lidos}")
    print(f"Total de ficheiros renomeados: {contador}")



if __name__ == "__main__":
    renomear_arquivos()