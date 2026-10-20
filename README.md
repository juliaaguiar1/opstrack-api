# OpsTrack API — Marco 1 (FATEC)

Disciplina: Integração e Entrega Contínua (ISW-032). Aplicação Flask com testes automatizados usando pytest.

## Rotas

`GET /`, `GET /status`, `GET /tickets`, `GET /sobre`, `GET /versao`, `GET /version` e `GET /usuarios`.

As cinco rotas originais foram preservadas. As rotas `/version` e `/usuarios` foram adicionadas para contemplar os exemplos e desafios do kit da Aula 06. Os dois usuários são dados demonstrativos, não um banco de dados.

## Rodando os testes

No Windows, abra o PowerShell na raiz do projeto:

```powershell
py -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\venv\Scripts\python.exe -m pytest -v
.\venv\Scripts\python.exe -m pytest --cov=app --cov-report=term-missing
.\venv\Scripts\python.exe -m pytest --cov=app --cov-fail-under=85
.\venv\Scripts\python.exe -m flake8 app.py tests
```

No Linux/macOS, ative com `source venv/bin/activate` e execute os mesmos comandos usando `python`.

## Meta de cobertura

A meta escolhida é **85%** de cobertura de linhas em `app.py`, seguindo a sugestão didática da Aula 06. O comando `--cov-fail-under=85` retorna erro caso a meta não seja alcançada, impedindo a aprovação de código com cobertura insuficiente. Cobertura mede execução, não ausência de defeitos: cada teste também possui `assert` para validar o comportamento. Não utilizamos `pragma: no cover` para elevar artificialmente a porcentagem.

O bloco `if __name__ == '__main__': app.run(debug=True)` não é acionado pelo cliente de testes do Flask, pois ele inicia um servidor real e não integra o fluxo de teste de rotas. Os percentuais e linhas não cobertas devem ser registrados a partir da execução efetiva, não presumidos.

## Desafio individual — evidências a registrar

1. O kit original começa com dois `COMPLETE AQUI`; seus exemplos indicam 3 aprovados e 2 reprovados antes da correção. Os testes deste projeto foram adaptados ao `app.py` real e já contêm as duas chamadas completas.
2. Para demonstrar falha funcional, altere temporariamente `/status` de `online` para `onlines`, execute pytest, capture a falha e restaure a alteração antes do commit. O flake8 não detecta essa mudança de comportamento.
3. Execute o relatório de cobertura e registre linhas não cobertas. Um bug na rota `/version` poderia informar a versão errada sem um teste de conteúdo. A linha `app.run(debug=True)` normalmente não precisa de cobertura por testes de rota, pois inicia o servidor diretamente.

## Versionamento e entrega

A atividade pede: suíte versionada por Pull Request, `pytest.ini`, `requirements-dev.txt`, README com instruções e justificativa da cobertura, pelo menos dois testes novos, repositório público e tag `marco-1` na `main` após o merge.


