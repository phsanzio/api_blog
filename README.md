# Blog API - Django RESTful

Este projeto é uma **API RESTful** para um **blog pessoal** desenvolvido com **Django** e **Django REST Framework (DRF)**. A API permite que você realize operações **CRUD (Criar, Ler, Atualizar e Deletar)** em postagens de blog, facilitando a interação com o banco de dados através de requisições HTTP em formato **JSON**.

### Tecnologias Utilizadas
- **Django**: Framework Python para desenvolvimento web.
- **Django REST Framework (DRF)**: Extensão do Django para criar APIs RESTful.
- **Python**: Linguagem de programação usada no backend.
- **SQLite** (padrão do Django): Banco de dados utilizado para armazenar os dados das postagens de blog.

### Funcionalidades da API
A API permite realizar as seguintes operações com as postagens do blog:

1. **Criar** uma nova postagem.
2. **Ler** todas as postagens ou uma postagem específica.
3. **Atualizar** uma postagem existente.
4. **Deletar** uma postagem.

### Endpoints

Aqui estão os endpoints disponíveis na API:

| Método  | Endpoint                           | Descrição                                  |
|---------|------------------------------------|--------------------------------------------|
| **GET** | `/posts/`                          | Retorna todas as postagens.                |
| **POST**| `/posts/create/`                   | Cria uma nova postagem.                   |
| **GET** | `/posts/<id>/`                     | Retorna uma postagem específica.           |
| **PUT** | `/posts/<id>/update/`              | Atualiza uma postagem existente.          |
| **DELETE**| `/posts/<id>/delete/`             | Deleta uma postagem existente.            |

### Requisitos

Para rodar este projeto, você precisa ter o **Python** instalado na sua máquina. Além disso, você precisará instalar as dependências utilizando o **pip**.

- Python 3.x
- Django
- Django REST Framework

### Instalação

Siga os passos abaixo para configurar e rodar o projeto:

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-usuario/blog-api-django.git
   cd blog-api-django
