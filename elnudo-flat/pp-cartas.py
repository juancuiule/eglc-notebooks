import pandas as pd
import numpy as np
import json

if __name__ == "__main__":
    jsonCartas = pd.read_json('./elnudo-cartas.json')

    keys = ["first", "second", "third", "allCorrect", "firstTime"]

    first = np.array([], dtype='bool_')
    second = np.array([], dtype='bool_')
    third = np.array([], dtype='bool_')
    allCorrect = np.array([], dtype='bool_')

    for x in jsonCartas["data"]:
        if np.all([k in x.keys() for k in keys]):
            if x["firstTime"]:
                first = np.append(first, x['first'])
                second = np.append(second, x['second'])
                third = np.append(third, x['third'])
                allCorrect = np.append(allCorrect, x['allCorrect'])
    df = pd.DataFrame({
        'first': first,
        'second': second,
        'third': third,
        'allCorrect': allCorrect
    })
    df.to_csv("cartas-contadas-raw-data.csv", index=True, header=["first", "second", "third", "allCorrect"])

    mean = df.mean() * 100

    data = {
        'first': mean['first'],
        'second': mean['second'],
        'third': mean['third'],
        'allCorrect': mean['allCorrect'],
        'total': len(df),
        'totalAllCorrect': len(df.loc[df['allCorrect']])
    }

    with open('./cartas-contadas.json', 'w') as fp:
        json.dump(data, fp)
