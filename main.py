# Mission Control Energy
# Global Solution 2026.1
# Soluções em Energias Renováveis e Sustentáveis

nome_missao = "Pathfinder-1 Energy"
nome_equipe = "ORION Control IA"

dados_missao = []


def analisar_temperatura(temperatura):
    if temperatura > 35:
        return "CRÍTICO", 2
    elif temperatura > 30:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_comunicacao(comunicacao):
    if comunicacao < 30:
        return "CRÍTICO", 2
    elif comunicacao < 60:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_bateria(bateria):
    if bateria < 20:
        return "CRÍTICO", 2
    elif bateria < 50:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_geracao_solar(geracao_solar):
    if geracao_solar < 30:
        return "CRÍTICO", 2
    elif geracao_solar < 60:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_status_modulo(status_modulo):
    if status_modulo < 40:
        return "CRÍTICO", 2
    elif status_modulo < 70:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def classificar_missao(pontuacao):

    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"

    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"

    else:
        return "MISSÃO CRÍTICA"


def cadastrar_ciclos():

    quantidade = int(input("Quantos ciclos deseja cadastrar? "))

    for i in range(quantidade):

        print()
        print(f"=== CADASTRO DO CICLO {i + 1} ===")

        temperatura = float(input("Temperatura (°C): "))
        comunicacao = int(input("Comunicação (%): "))
        bateria = int(input("Bateria (%): "))
        geracao_solar = int(input("Geração Solar (%): "))
        status_modulo = int(input("Status dos Módulos (%): "))

        ciclo = [
            temperatura,
            comunicacao,
            bateria,
            geracao_solar,
            status_modulo
        ]

        dados_missao.append(ciclo)


def analisar_missao():

    maior_risco = 0
    ciclo_mais_critico = 0
    soma_riscos = 0

    print()
    print("=" * 60)
    print("MISSION CONTROL ENERGY")
    print("=" * 60)
    print(f"Missão: {nome_missao}")
    print(f"Equipe: {nome_equipe}")
    print("=" * 60)

    for i in range(len(dados_missao)):

        temperatura = dados_missao[i][0]
        comunicacao = dados_missao[i][1]
        bateria = dados_missao[i][2]
        geracao_solar = dados_missao[i][3]
        status_modulo = dados_missao[i][4]

        status_temp, risco_temp = analisar_temperatura(temperatura)
        status_com, risco_com = analisar_comunicacao(comunicacao)
        status_bat, risco_bat = analisar_bateria(bateria)
        status_sol, risco_sol = analisar_geracao_solar(geracao_solar)
        status_mod, risco_mod = analisar_status_modulo(status_modulo)

        pontuacao = (
            risco_temp +
            risco_com +
            risco_bat +
            risco_sol +
            risco_mod
        )

        soma_riscos += pontuacao

        if pontuacao > maior_risco:
            maior_risco = pontuacao
            ciclo_mais_critico = i + 1

        classificacao = classificar_missao(pontuacao)

        print()
        print(f"CICLO {i + 1}")
        print("-" * 50)

        print(f"Temperatura: {temperatura}°C - {status_temp}")
        print(f"Comunicação: {comunicacao}% - {status_com}")
        print(f"Bateria: {bateria}% - {status_bat}")
        print(f"Geração Solar: {geracao_solar}% - {status_sol}")
        print(f"Status dos Módulos: {status_modulo}% - {status_mod}")

        print(f"Pontuação de risco: {pontuacao}")
        print(f"Classificação: {classificacao}")

        if pontuacao > 5:
            print("Ação: Ativar modo de economia de energia.")

        elif pontuacao > 2:
            print("Ação: Monitorar sistemas energéticos.")

        else:
            print("Ação: Operação normal.")

    risco_medio = soma_riscos / len(dados_missao)

    print()
    print("=" * 60)
    print("RELATÓRIO FINAL")
    print("=" * 60)

    print(f"Ciclo mais crítico: {ciclo_mais_critico}")
    print(f"Maior risco encontrado: {maior_risco}")
    print(f"Risco médio: {risco_medio:.2f}")

    if risco_medio <= 2:
        print("Resultado Final: MISSÃO ESTÁVEL")

    elif risco_medio <= 5:
        print("Resultado Final: MISSÃO EM ATENÇÃO")

    else:
        print("Resultado Final: MISSÃO CRÍTICA")

    print()
    print("Conclusão:")
    print("O sistema recebeu dados informados pelo usuário e monitorou")
    print("temperatura, comunicação, bateria, geração solar e status")
    print("dos módulos da missão espacial.")
    print("Com base nesses dados, foram gerados alertas e ações")
    print("voltadas ao uso eficiente da energia e sustentabilidade.")


cadastrar_ciclos()
analisar_missao()