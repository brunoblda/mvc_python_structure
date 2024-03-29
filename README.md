# 1. MVC (Model View Controller)

## 1.1 Geral

Programador lhama - playlist - Padrão MVC em Python
[Link to YouTube playlist](https://www.youtube.com/playlist?list=PLAgbpJQADBGKvsjOu4gHU5E9WUQs8XRgS)

## 1.2 Conteúdo

Model - Manipulação de dados
View - Interação do usuário
Controller - Camada de controle

A pasta main realiza a conexão entre a model, a view e o controller.

### 1.2.1 Main

Main contém

- constructor - contruir o processo
- process_handle - disponibilizar

O constructor junta a view com o controller e se possível com o model

### 1.2.2 View

View não tem logica, somente troca de informações

### 1.2.3 Controller

Controllers é onde ficam as regras de negocios ou casos de uso

### 1.2.4 Models

Models conversa com o banco, csv ou xlsx

Entities
Representa o que vai estar no banco de dados

Repository
Elementos básicos para interagir com o banco

Connections
Conexão com o banco de dados, verifica se um arquivo csv ou banco existe