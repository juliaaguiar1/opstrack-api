"""Testes da API OpsTrack: kit Aula 06 adaptado e ampliado."""


def test_raiz_informa_servico_online(client):
    resposta = client.get('/')
    assert resposta.status_code == 200
    assert resposta.get_json() == {'mensagem': 'OpsTrack API funcionando!'}


def test_status_retorna_online(client):
    resposta = client.get('/status')
    assert resposta.status_code == 200
    assert resposta.get_json()['status'] == 'online'


def test_tickets_retorna_lista_com_id_e_titulo(client):
    resposta = client.get('/tickets')
    assert resposta.status_code == 200
    tickets = resposta.get_json()['tickets']
    assert len(tickets) == 2
    assert 'id' in tickets[0]
    assert 'titulo' in tickets[0]


def test_usuarios_retorna_dois_usuarios(client):
    resposta = client.get('/usuarios')  # COMPLETE AQUI resolvido
    assert resposta.status_code == 200
    assert len(resposta.get_json()['usuarios']) == 2


def test_rota_inexistente_retorna_404(client):
    resposta = client.get('/nao-existe')  # COMPLETE AQUI resolvido
    assert resposta.status_code == 404


def test_version_retorna_versao(client):
    resposta = client.get('/version')
    assert resposta.status_code == 200
    assert resposta.get_json()['versao'] == '1.0.0'


def test_sobre_retorna_dados(client):
    resposta = client.get('/sobre')
    assert resposta.status_code == 200
    assert resposta.get_json() == {'nome': 'OpsTrack API', 'versao': '1.0.0'}


def test_versao_original_continua_funcionando(client):
    resposta = client.get('/versao')
    assert resposta.status_code == 200
    assert resposta.get_json()['versao'] == '1.0.0'


def test_tickets_tem_campos_e_status_validos(client):
    resposta = client.get('/tickets')
    assert resposta.status_code == 200
    for ticket in resposta.get_json()['tickets']:
        assert set(ticket) == {'id', 'titulo', 'status'}
        assert isinstance(ticket['id'], int)
        assert ticket['titulo']
        assert ticket['status'] in {'aberto', 'fechado'}


def test_status_rejeita_post(client):
    resposta = client.post('/status')
    assert resposta.status_code == 405
