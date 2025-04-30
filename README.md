# Blog API - Django RESTful

API RESTful para um blog pessoal desenvolvida com Django e DRF. Permite operações CRUD em postagens via requisições HTTP em formato JSON.

## Tecnologias

-   Django
-   Django REST Framework (DRF)
-   Python
-   SQLite

## Funcionalidades

-   Criar, Ler, Atualizar e Deletar postagens.

## Endpoints

| Método   | Endpoint                           | Descrição                                    |
| :-------- | :--------------------------------- | :------------------------------------------- |
| GET    | `/posts/`                          | Retorna todas as postagens.                  |
| POST   | `/posts/create/`                   | Cria uma nova postagem.                     |
| GET    | `/posts/<id>/`                     | Retorna uma postagem específica.             |
| PUT    | `/posts/<id>/update/`              | Atualiza uma postagem existente.            |
| DELETE | `/posts/<id>/delete/`             | Deleta uma postagem existente.              |

## Requisitos

-   Python 3.x
-   Django
-   Django REST Framework

## Instalação

1.  Clone:
    ```bash
    git clone [https://github.com/seu-usuario/blog-api-django.git](https://github.com/seu-usuario/blog-api-django.git)
    cd blog-api-django
    ```
2.  Virtual env (opcional):
    ```bash
    python -m venv venv
    source venv/bin/activate # macOS/Linux
    venv\Scripts\activate    # Windows
    ```
3.  Dependências:
    ```bash
    pip install -r requirements.txt
    ```
4.  Migrações:
    ```bash
    python manage.py migrate
    ```
5.  Superusuário (opcional):
    ```bash
    python manage.py createsuperuser
    ```
6.  Servidor:
    ```bash
    python manage.py runserver
    ```
    Disponível em http://127.0.0.1:8000/

## Testando a API

Use Postman/cURL:

### Criar Post (POST /posts/create/)

```json
{
    "title": "Postagem 1",
    "content": "Conteúdo da postagem.",
    "category": "Categoria",
    "tags": ["Tag1", "Tag2"]
}
```

### Listar Posts (GET /posts/)

### Detalhar Post (GET /posts/1/)

### Atualizar Post (PUT /posts/1/update/)

```json
{
    "title": "Postagem Atualizada",
    "content": "Novo conteúdo.",
    "category": "Nova Categoria",
    "tags": ["NovaTag"]
}
```

### Deletar Post (DELETE /posts/1/delete/)

Criado por: Pedro Sanzio
