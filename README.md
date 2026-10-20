# OpsTrack API — Marco 1

**Faculdade:** FATEC  
**Disciplina:** Integração e Entrega Contínua (ISW-032)  
**Atividade:** Desafio em Equipe — Aula 06  
**Projeto:** OpsTrack API  
**Tecnologia principal:** Python e Flask

## 1. Apresentação do projeto

O OpsTrack API é uma aplicação desenvolvida em Python utilizando o framework Flask. O projeto disponibiliza rotas HTTP para consulta de informações demonstrativas, como status do serviço, tickets, usuários e versão da aplicação.

O Marco 1 tem como objetivo implementar e organizar testes automatizados, avaliar a cobertura do código e aplicar boas práticas de versionamento utilizando Git e GitHub.

A atividade também busca demonstrar a importância dos testes no processo de integração contínua, contribuindo para a identificação de falhas e para a manutenção da qualidade do software.

## 2. Tecnologias e ferramentas utilizadas

- **Python:** linguagem de programação utilizada no desenvolvimento da aplicação.
- **Flask:** framework responsável pela implementação das rotas HTTP.
- **pytest:** ferramenta utilizada na execução dos testes automatizados.
- **pytest-cov:** extensão responsável pela medição da cobertura dos testes.
- **flake8:** ferramenta de análise estática e padronização do código Python.
- **Git:** sistema de controle de versão.
- **GitHub:** plataforma utilizada para hospedagem do repositório e gerenciamento do Pull Request.

## 3. Rotas disponíveis

A aplicação disponibiliza as seguintes rotas:

| Método | Rota | Descrição |
|---|---|---|
| GET | `/` | Retorna informações sobre o serviço |
| GET | `/status` | Retorna o status da aplicação |
| GET | `/tickets` | Retorna uma lista demonstrativa de tickets |
| GET | `/usuarios` | Retorna uma lista demonstrativa de usuários |
| GET | `/sobre` | Retorna informações sobre o projeto |
| GET | `/versao` | Retorna a versão da aplicação |
| GET | `/version` | Disponibiliza uma rota adicional de consulta à versão |

As cinco rotas originais foram preservadas. As rotas `/usuarios` e `/version` foram incluídas para contemplar os testes e desafios propostos na atividade.

Os dados apresentados são demonstrativos e não dependem de um banco de dados.

## 4. Estrutura dos arquivos

Os principais arquivos utilizados no Marco 1 são:

| Arquivo ou pasta | Finalidade |
|---|---|
| `app.py` | Implementação da aplicação Flask |
| `tests/conftest.py` | Configuração das estruturas de apoio aos testes |
| `tests/test_api.py` | Implementação dos testes automatizados |
| `pytest.ini` | Configuração do pytest |
| `requirements.txt` | Dependências principais da aplicação |
| `requirements-dev.txt` | Dependências necessárias ao desenvolvimento e aos testes |
| `.flake8` | Configuração da análise estática |
| `.pre-commit-config.yaml` | Configuração de verificações associadas ao pre-commit |
| `.gitignore` | Exclusão de arquivos temporários do versionamento |
| `README.md` | Documentação do projeto |

## 5. Preparação do ambiente

Para executar o projeto localmente, é necessário ter o Python instalado.

Primeiramente, clone o repositório:

```bash
git clone https://github.com/juliaaguiar1/opstrack-api.git
```

Entre na pasta do projeto:

```bash
cd opstrack-api
```

### 5.1. Configuração no Windows

Crie o ambiente virtual:

```powershell
py -m venv venv
```

Instale as dependências:

```powershell
.\venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

### 5.2. Configuração no Linux ou macOS

Crie e ative o ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install -r requirements-dev.txt
```

## 6. Rodando os testes

Os testes automatizados foram implementados com pytest e estão organizados na pasta `tests/`.

### 6.1. Executar os testes no Windows

```powershell
.\venv\Scripts\python.exe -m pytest -v
```

### 6.2. Executar os testes no Linux ou macOS

Com o ambiente virtual ativado:

```bash
python -m pytest -v
```

A opção `-v` apresenta informações detalhadas sobre a execução, incluindo o resultado individual de cada teste.

### 6.3. Executar os testes com cobertura

No Windows:

```powershell
.\venv\Scripts\python.exe -m pytest --cov=app --cov-report=term-missing --cov-fail-under=85
```

No Linux ou macOS:

```bash
python -m pytest --cov=app --cov-report=term-missing --cov-fail-under=85
```

Os parâmetros utilizados possuem as seguintes funções:

- `--cov=app`: mede a cobertura do módulo `app.py`.
- `--cov-report=term-missing`: apresenta a porcentagem de cobertura e as linhas não executadas.
- `--cov-fail-under=85`: estabelece uma cobertura mínima de 85%, fazendo com que a verificação falhe caso o resultado seja inferior ao limite definido.

## 7. Testes automatizados implementados

A suíte contém 10 testes automatizados:

| Teste | Objetivo |
|---|---|
| `test_raiz_informa_servico_online` | Verificar as informações retornadas pela rota principal |
| `test_status_retorna_online` | Validar o status retornado pela aplicação |
| `test_tickets_retorna_lista_com_id_e_titulo` | Verificar a estrutura dos tickets |
| `test_usuarios_retorna_dois_usuarios` | Confirmar o retorno de dois usuários |
| `test_rota_inexistente_retorna_404` | Verificar o tratamento de rotas inexistentes |
| `test_version_retorna_versao` | Validar a rota adicional de versão |
| `test_sobre_retorna_dados` | Verificar as informações da rota `/sobre` |
| `test_versao_original_continua_funcionando` | Garantir o funcionamento da rota `/versao` |
| `test_tickets_tem_campos_e_status_validos` | Validar os campos e valores dos tickets |
| `test_status_rejeita_post` | Verificar a rejeição de uma requisição POST na rota `/status` |

Os testes verificam respostas HTTP, estruturas de dados, conteúdos retornados e comportamentos esperados das rotas.

## 8. Resultados dos testes

A execução realizada localmente, utilizando Python 3.13.2 e pytest 9.1.1, apresentou os seguintes resultados:

| Indicador | Resultado |
|---|---|
| Total de testes | 10 |
| Testes aprovados | 10 |
| Testes reprovados | 0 |
| Cobertura de `app.py` | 96% |
| Meta mínima | 85% |
| Linhas de código consideradas | 25 |
| Linhas não executadas | 1 |

Relatório de cobertura obtido:

```text
Name     Stmts   Miss  Cover   Missing
--------------------------------------
app.py      25      1    96%   48
--------------------------------------
TOTAL       25      1    96%

Required test coverage of 85% reached.
Total coverage: 96.00%

10 passed
```

Os resultados demonstram que todos os testes implementados foram aprovados e que a cobertura alcançada ultrapassou a meta estabelecida.

## 9. Justificativa da meta de cobertura

A meta mínima definida para o projeto foi de **85% de cobertura de linhas**, considerando o escopo da aplicação e as orientações didáticas da Aula 06.

Esse percentual foi escolhido por representar um objetivo de qualidade que permite verificar a maior parte do comportamento implementado, sem considerar que a cobertura, isoladamente, garante a ausência de defeitos.

A cobertura indica quais linhas foram executadas durante os testes, mas não comprova que todas as situações possíveis foram verificadas. Por esse motivo, os testes também utilizam asserções para comparar os resultados obtidos com os comportamentos esperados.

A utilização do parâmetro `--cov-fail-under=85` permite estabelecer uma verificação objetiva, que poderá ser incorporada a um processo de integração contínua.

### 9.1. Análise da linha não coberta

Na execução realizada, a cobertura foi de 96%, com a linha 48 do arquivo `app.py` não executada.

Essa linha corresponde à inicialização do servidor Flask por meio de `app.run(debug=True)`.

Os testes utilizam o cliente de testes do Flask, que permite realizar requisições sem iniciar o servidor da aplicação. Por esse motivo, a execução direta do servidor não faz parte do fluxo testado.

Não foi utilizada a instrução `pragma: no cover` para aumentar artificialmente o percentual de cobertura.

## 10. Análise estática com flake8

Além dos testes funcionais, o projeto utiliza flake8 para identificar problemas de estilo e determinadas inconsistências no código Python.

Para executar a verificação no Windows:

```powershell
.\venv\Scripts\python.exe -m flake8 .
```

No Linux ou macOS:

```bash
python -m flake8 .
```

A execução realizada localmente não apresentou mensagens de erro.

É importante destacar que o flake8 não substitui os testes automatizados, pois sua finalidade é analisar aspectos estáticos do código, e não verificar se as rotas retornam os resultados funcionalmente corretos.

## 11. Desafio individual — análise e evidências

A atividade também propõe exercícios relacionados à identificação de falhas, correção de testes e interpretação dos resultados.

### 11.1. Complementação dos testes

O material inicial disponibilizado para a atividade continha dois trechos indicados como `COMPLETE AQUI`.

Esses trechos foram completados e os testes foram adaptados ao comportamento da aplicação utilizada no projeto.

A suíte final contém 10 testes automatizados aprovados.

### 11.2. Identificação de falhas funcionais

Uma alteração indevida no conteúdo retornado por uma rota pode provocar a falha de um teste automatizado.

Por exemplo, caso o valor esperado na rota `/status` seja alterado incorretamente, um teste que verifica o conteúdo da resposta poderá identificar a divergência.

Esse tipo de situação demonstra a importância de verificar não apenas o código de status HTTP, mas também os dados retornados pela aplicação.

A realização de um experimento com falha proposital deve ser registrada separadamente, caso seja exigida como evidência da atividade.

### 11.3. Interpretação da cobertura

O relatório de cobertura permite identificar quais partes do código foram executadas durante os testes.

No projeto, o resultado de 96% indica que a maior parte das instruções de `app.py` foi executada.

Entretanto, a existência de uma cobertura elevada não elimina a necessidade de elaborar testes relevantes, especialmente para situações de erro, validação de dados e comportamentos inesperados.

## 12. Versionamento com Git e GitHub

O desenvolvimento do Marco 1 foi realizado utilizando uma branch específica para as alterações:

```text
feature/testes
```

Após a implementação e validação dos testes, as alterações foram registradas em commit e enviadas ao repositório remoto.

Em seguida, foi criado o Pull Request nº 1, responsável pela integração da branch `feature/testes` à branch principal `main`.

O Pull Request foi mesclado com sucesso, preservando o histórico de desenvolvimento.

### 12.1. Identificação da entrega

Após a integração das alterações, foi criada e publicada a tag:

```text
marco-1
```

Essa tag identifica a versão do projeto correspondente à entrega do primeiro marco.

### 12.2. Repositório

**GitHub:** https://github.com/juliaaguiar1/opstrack-api

**Pull Request:** https://github.com/juliaaguiar1/opstrack-api/pull/1

**Tag:** https://github.com/juliaaguiar1/opstrack-api/releases/tag/marco-1

## 13. Considerações finais

A implementação do Marco 1 permitiu aplicar conceitos de testes automatizados, cobertura de código, análise estática e controle de versão em uma aplicação Flask.

A suíte desenvolvida apresentou 10 testes aprovados e 96% de cobertura, superando a meta mínima de 85% estabelecida para o projeto.

O uso de uma branch específica e de um Pull Request também contribuiu para organizar as alterações e registrar sua integração à versão principal do repositório.

Dessa forma, o projeto demonstra a aplicação prática de procedimentos que auxiliam na identificação de problemas, na manutenção do software e na preparação de processos de integração contínua.

