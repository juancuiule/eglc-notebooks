import pandas as pd
# import numpy as np
# from scipy import stats
import matplotlib.pyplot as plt

if __name__ == "__main__":
    json = pd.read_json('./libet-data.json')
    
    raw = []
    for x in json["data"]:
        if "pc" in x.keys() and "user" in x.keys() and "won" in x.keys():
            pc = x["pc"]
            user = x["user"]
            won = x["won"]
            if pc > 0 and pc <= 50 and user <= 50 and (won == "pc" or won == "user"):
                raw.append([pc, user, won])
    pd.DataFrame(raw).to_csv("libet-raw-data.csv", index=True, header=["pc", "user", "won"])
    
    df = pd.DataFrame(raw, columns=["pc", "user", "won"])

    values = pd.Series(df["user"]).value_counts()
    total_partidas = len(df)
    ganadas_pc = df["won"].value_counts()["pc"]
    porcentaje_pc_win = int(ganadas_pc / total_partidas * 100)
    histograma = []
    acum = 0
    for x in range(0, 51):
        p_con_menos_x = int(acum / total_partidas * 100)
        if x in values.keys():
            p_con_x = values[x]
            histograma.append([x, p_con_x, total_partidas, porcentaje_pc_win, p_con_menos_x])
            acum += p_con_x
        else:
            histograma.append([x, 0, total_partidas, porcentaje_pc_win, p_con_menos_x])

    header = [
        "puntos",
        "partidas",
        "total_partidas",
        "porcentaje_pc",
        "porcentaje_con_menos"
    ]
    pd.DataFrame(histograma).to_csv("libet.csv", index=False, header=header)

    df["user"].hist(grid=False, bins=50)
    plt.xlabel('Puntos usuarie')
    plt.ylabel('Número de partidas')
    plt.title('Puntos de usuaries por partida')
    plt.savefig("hist.png")
