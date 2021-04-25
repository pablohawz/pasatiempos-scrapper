import pandas as pd


def split1(x):

    if ',' in x:
        return x.split(',')[0]

    if 'que' in x:
        return x.split('que')[0]

    parts = x.split(' ')
    mid = int(len(parts)/2)
    half_parts = x.split(' ')[:mid]
    s = ''
    for part in half_parts:
        s = s+part+' '
    return s

def split2(x):

    if ',' in x:
        return x.split(',')[1]

    if 'que' in x:
        return 'que' + x.split('que')[1]

    parts = x.split(' ')
    mid = int(len(parts)/2)
    half_parts = x.split(' ')[mid:]
    s = ''
    for part in half_parts:
        s = s+part+' '
    return s


df = pd.read_csv('refranes.csv')
df['refran_completo'] = df['Refran'].apply(lambda x: x.replace('"', ''))

df['parte_1'] = df['refran_completo'].apply(split1)
df['parte_2'] = df['refran_completo'].apply(split2)

