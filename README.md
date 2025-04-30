# Blog API - Django RESTful

Este projeto é uma **API RESTful** para um **blog pessoal** desenvolvido com **Django** e **Django REST Framework (DRF)**. A API permite que você realize operações **CRUD (Criar, Ler, Atualizar e Deletar)** em postagens de blog, facilitando a interação com o banco de dados através de requisições HTTP em formato **JSON**.

## Tecnologias Utilizadas

-   **Django**: Framework Python para desenvolvimento web.
-   **Django REST Framework (DRF)**: Extensão do Django para criar APIs RESTful.
-   **Python**: Linguagem de programação usada no backend.
-   **SQLite** (padrão do Django): Banco de dados utilizado para armazenar os dados das postagens de blog.

## Funcionalidades da API

A API permite realizar as seguintes operações com as postagens do blog:

1.  **Criar** uma nova postagem.
2.  **Ler** todas as postagens ou uma postagem específica.
3.  **Atualizar** uma postagem existente.
4.  **Deletar** uma postagem.

## Endpoints

Aqui estão os endpoints disponíveis na API:

| Método   | Endpoint                           | Descrição                                    |
| :-------- | :--------------------------------- | :------------------------------------------- |
| **GET** | `/posts/`                          | Retorna todas as postagens.                  |
| **POST** | `/posts/create/`                   | Cria uma nova postagem.                     |
| **GET** | `/posts/<id>/`                     | Retorna uma postagem específica.             |
| **PUT** | `/posts/<id>/update/`              | Atualiza uma postagem existente.            |
| **DELETE** | `/posts/<id>/delete/`             | Deleta uma postagem existente.              |

## Requisitos

Para rodar este projeto, você precisa ter o **Python** instalado na sua máquina. Além disso, você precisará instalar as dependências utilizando o **pip**.

-   Python 3.x
-   Django
-   Django REST Framework

## Instalação

Siga os passos abaixo para configurar e rodar o projeto:

1.  **Clone o repositório**:

    ```bash
    git clone [https://github.com/seu-usuario/blog-api-django.git](https://github.com/seu-usuario/blog-api-django.git)
    cd blog-api-django
    ```

2.  Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    ```

3.  Ative o ambiente virtual:

    No Windows:

    ```bash
    venv\Scripts\activate
    ```

    No macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

4.  Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

5.  Crie as migrações e migre o banco de dados:

    ```bash
    python manage.py migrate
    ```

6.  Crie um superusuário (opcional, para acessar o Django Admin):

    ```bash
    python manage.py createsuperuser
    ```

7.  Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

    A API estará disponível em: http://127.0.0.1:8000/

## Testando a API

Agora você pode testar a API com ferramentas como Postman ou cURL.

Criar uma nova postagem (POST):

```bash
POST /posts/create/
Content-Type: application/json

{
    "title": "My First Blog Post",
    "content": "This is the content of my first blog post.",
    "category": "Technology",
    "tags": ["Tech", "Programming"]
}
```

Obter todas as postagens (GET):

```bash
GET /posts/
```

Obter uma postagem específica (GET):

```bash
GET /posts/1/
```

Atualizar uma postagem (PUT):

```bash
PUT /posts/1/update/
Content-Type: application/json

{
    "title": "Updated Title",
    "content": "Updated content",
    "category": "New Category",
    "tags": ["NewTag"]
}
```

Deletar uma postagem (DELETE):

```bash
DELETE /posts/1/delete/
```

## Contribuindo

Se você deseja contribuir para este projeto, fique à vontade para fazer um fork, criar uma branch e enviar um pull request.

## Licença

Este projeto é licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.


Criado por: Pedro Sanzio
