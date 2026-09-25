def filtrar_livros(lista_livros, **criterios):
    """
    Filtra uma lista de dicionários de livros com base nos critérios fornecidos.

    :param lista_livros: Lista de dicionários contendo os dados dos livros.
    :param criterios: Argumentos nomeados (kwargs) representando os filtros (ex: autor="...", genero="...").
    :return: Lista contendo apenas os livros que correspondem a TODOS os critérios.
    """
    livros_filtrados = []

    for livro in lista_livros:
        corresponde = True

        # Verifica se o livro atende a cada um dos critérios solicitados
        for chave, valor_buscado in criterios.items():
            if livro.get(chave) != valor_buscado:
                corresponde = False
                break

        if corresponde:
            livros_filtrados.append(livro)

    return livros_filtrados
