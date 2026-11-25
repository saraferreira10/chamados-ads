# API de Chamados de Suporte

## 1. Estudante
Sara Ferreira de Araújo

## 2. Objetivo do Projeto
Criar a estrutura inicial da API de chamados de suporte utilizando Python, Flask e o gerenciador de dependências `uv`, reproduzindo o desenvolvimento apresentado na videoaula "Criando a primeira API com Flask".

## 3. Como Instalar as Dependências
Certifique-se de ter o `uv` instalado em seu ambiente e execute o comando abaixo na raiz do projeto:

```bash
uv sync --locked

```

## 4. Como Executar a Aplicação

Para iniciar o servidor da aplicação (incluindo ambientes como o GitHub Codespaces), execute:

```bash
uv run flask --app app run --host=0.0.0.0 --port=5000

```

## 5. Como Acessar as Rotas e Respostas Esperadas

Com o servidor em execução, utilize o navegador ou o terminal para testar os endpoints:

### Semana 01
- **Rota Inicial (`GET /`)**
  - **Comando:** `curl -i http://localhost:5000/`
  - **Resposta esperada:** Status `200 OK`, cabeçalho `Content-Type: application/json` e o corpo:
    ```json
    {
      "mensagem": "API de chamados em funcionamento"
    }
    ```

### Semana 02
- **Listar Chamados (`GET /chamados`)**
  - **Comando:** `curl -i http://localhost:5000/chamados`
  - **Resposta esperada:** Status `200 OK` e um array JSON contendo os chamados cadastrados (ou `[]` se estiver vazio).

- **Consultar Chamado por ID (`GET /chamados/{id}`)**
  - **Comando:** `curl -i http://localhost:5000/chamados/1`
  - **Resposta esperada:** Status `200 OK` com os dados do chamado correspondente, ou `404 Not Found` contendo `{"mensagem": "Chamado não encontrado"}` caso o ID não exista.

- **Cadastrar Chamado (`POST /chamados`)**
  - **Comando (exemplo via terminal):**
    ```bash
    curl -i -X POST http://localhost:5000/chamados 
      -H "Content-Type: application/json" 
      -d "{\"titulo\": \"Impressora sem conexão\", \"descricao\": \"A impressora do laboratório não aparece na rede.\", \"solicitante\": \"Ana\", \"prioridade\": \"media\"}"
    ```
  - **Corpo enviado (JSON):**
    ```json
    {
      "titulo": "Impressora sem conexão",
      "descricao": "A impressora do laboratório não aparece na rede.",
      "solicitante": "Ana",
      "prioridade": "media"
    }
    ```
  - **Resposta esperada:** Status `201 Created` contendo o chamado criado com o ID gerado e o status inicial `"aberto"`.

## 6. Checklist de Verificação da Entrega

### 📌 Semana 01
- [x] A instalação das dependências funciona seguindo o README.
- [x] A aplicação inicia sem erros.
- [x] Uma requisição `GET /` retorna status 200.
- [x] A resposta possui o cabeçalho `Content-Type` indicando `application/json`.
- [x] O corpo contém o objeto JSON solicitado.

### 📌 Semana 02
- [x] A rota `POST /chamados` cadastra em memória gerando ID automático e status `"aberto"`, retornando status `201`.
- [x] A rota `GET /chamados` lista todos os chamados cadastrados ou retorna `[]`.
- [x] A rota `GET /chamados/{id}` retorna o chamado correto (status 200) ou mensagem de erro com status `404`.
- [x] As respostas mantêm o cabeçalho `Content-Type: application/json`.
