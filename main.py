import requests

# Função para fazer o get() na API
def get_response(nome):
    # Url da Brasil API
    url = 'https://brasilapi.com.br/api/taxas/v1'
    response = requests.get(url)
    # Status HTTP
    if response.status_code == 200:
        data = response.json()
        for i in data:
            if i.get("nome", None) == nome:
                return i
        return f'Indice {nome} não encontrado'
    else:
        return f'Erro na solicitação da API {response.status_code}'

def main():
    nome = input('Digite o nome do índice que deseja pesquisar (EX: CDI, Selic): ')
    response_content = get_response(nome)
    if isinstance(response_content, str):
        print(response_content)
    else:
        print(f'{response_content["nome"]} - {response_content["valor"]}')

if __name__ == "__main__":
    main()