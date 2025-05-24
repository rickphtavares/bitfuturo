# BitFuturo - Plataforma Educacional de Capacitação Digital

BitFuturo é um sistema educacional simulado, desenvolvido como parte do Projeto Integrado Multidisciplinar (PIM) do curso de Análise e Desenvolvimento de Sistemas da UNIP. O objetivo é representar uma plataforma de ensino voltada à inclusão digital, especialmente de comunidades em vulnerabilidade social.

## Funcionalidades Implementadas

* Cadastro de usuário com validação de dados (nome, CPF, idade, e-mail, celular e senha forte);
* Login com autenticação via e-mail ou CPF;
* Listagem de cursos disponíveis;
* Inscrição do aluno em cursos com limite de dois cursos em andamento;
* Finalização de cursos e geração de certificados;
* Menu do aluno: visualização de dados pessoais, cursos inscritos e certificados conquistados;
* Menu do administrador: adicionar, editar, excluir e visualizar cursos, além de consultar a lista de usuários.

## Armazenamento de Dados

Todos os dados são armazenados em arquivos `.json`:

* `usuarios.json`: armazena os dados dos alunos cadastrados;
* `cursos.json`: lista de cursos disponíveis;
* `seguranca.txt`: conteúdo informativo sobre segurança digital.

## Requisitos de Execução

* Python 3.x
* Biblioteca padrão `json` e `hashlib`

## Execução

Para executar o sistema, basta rodar o arquivo `CódigoPIM.py` com Python.

```bash
python CódigoPIM.py
```

## Credenciais de Administração

* **Usuário**: `adminbit`
* **Senha**: `administradorinstitutobit250524`

## Autoria

Desenvolvido por:

* Henrique Oliveira Tavares
* Pedro Henrique Tavares de Oliveira
* Leticia Oliveira Silva
* Miguel de Oliveira
* Vinicius Mazieri e Silva

UNIP - Universidade Paulista
Curso de Análise e Desenvolvimento de Sistemas

---

> Este projeto simula uma solução real de impacto social através da tecnologia. Todos os dados e nomes utilizados para cadastro de usuários são fictícios.
