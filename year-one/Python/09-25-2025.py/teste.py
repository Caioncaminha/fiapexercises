import json

def pega_dados():
    with open('ano2018.json') as f:
        dados = json.load(f)
    return dados

dados2018 = pega_dados()

def id_do_time(dados,nome_time):
    dic = dados['equipes']
    for id_time in dic.keys():
        time = (dados['equipes'][id_time]['nome-comum'])
        if time == nome_time:
            return id_time
    return 'nao achei'

def placar_por_time(dados, input1, input2):
    dic_ids = dados['2700']['jogos']['id']
    (id_time1,id_time2) = (id_do_time(dados, input1), id_do_time(dados, input2))
    for id_jogo in dic_ids.keys():
    (gol1,gol2) = ([id_jogo]['placar1'], [id_jogo]['placar2'])
    return print(f"{time1} {gol1} x {gol2} {time2}")
