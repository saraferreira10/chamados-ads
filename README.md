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

## 5. Como Acessar a Rota Inicial e Resposta Esperada

Com o servidor em execução, acesse `http://localhost:5000/` pelo navegador ou faça uma requisição pelo terminal utilizando:

```bash
curl -i http://localhost:5000/

```

**Resposta esperada:**

* **Status HTTP:** `200 OK`
* **Cabeçalho:** `Content-Type: application/json`
* **Corpo da resposta (JSON):**
```json
{
  "mensagem": "API de chamados em funcionamento"
}

```

## 6. Checklist de Verificação da Entrega
- [x] A instalação das dependências funciona seguindo o README.
- [x] A aplicação inicia sem erros.
- [x] Uma requisição GET / retorna status 200.
- [x] A resposta possui o cabeçalho Content-Type indicando application/json.
- [x] O corpo contém o objeto JSON solicitado.
