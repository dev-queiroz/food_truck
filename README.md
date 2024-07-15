# Food Trucks API

## Descrição
Este projeto fornece informações sobre food trucks disponíveis perto de uma localização específica e os exibe em um mapa.

## Tecnologias Usadas
- Python
- Flask
- Requests
- Leaflet.js
- OpenStreetMap

## Configuração
1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/food_trucks.git
    ```
2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3. Execute a aplicação:
    ```bash
    python app.py
    ```

## Endpoints da API
- `GET /`: Renderiza a página inicial com o mapa.
- `GET /food-trucks`: Retorna em formato JSON, todos os food trucks perto de uma localização específica.
    - Parâmetros: `latitude` e `longitude`
    - Exemplo: `/food-trucks?latitude=37.7749&longitude=-122.4194`
