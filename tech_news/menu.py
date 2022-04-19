import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (
    search_by_category, search_by_date, search_by_source, search_by_title
)


# Requisito 12
def analyzer_menu():
    my_menu = (
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair."
    )
    print(my_menu)

    option = input()

    dict_option = {
        0: "Digite quantas notícias serão buscadas:",
        1: "Digite o título:",
        2: "Digite a data no formato aaaa-mm-dd:",
        3: "Digite a fonte:",
        4: "Digite a categoria:",
        5: "Digite quantas notícias serão buscadas:"
    }

    dict_functions = {
        "0": get_tech_news,
        "1": search_by_title,
        "2": search_by_date,
        "3": search_by_source,
        "4": search_by_category,
        "5": top_5_news(),
        "6": top_5_categories(),
    }

    if(option.isdigit() and -1 < int(option) < 5):
        print(dict_option[int(option)])
        answer = input()
        print(dict_functions[option](answer))
    elif(option.isdigit() and 4 < int(option) < 7):
        print(dict_functions[option])
    elif (option.isdigit() and int(option) == 7):
        print("Encerrando script")
        sys.stdin.close()
    else:
        print("Opção inválida", file=sys.stderr)
