from py2neo import Graph, Node, Relationship
import pandas as pd
import io
import requests


def load_json_as_panda():
    structure_url = 'https://data.enseignementsup-recherche.gouv.fr/explore/dataset/' \
                    'fr-esr-structures-recherche-publiques-actives/download/?format=json'
    structure_csv_raw = requests.get(structure_url).content
    structures = pd.read_json(io.StringIO(structure_csv_raw.decode('utf-8')))
    return structures['fields'].values


def split_me(s, label):
    v = s.get(label, '').split(';')
    return v if len(v) else None

records = load_json_as_panda()

tutelles = {x for s in records for x in split_me(s,'tutelles') if x}
print(tutelles)
nodes_tutelles = [Node('Tutelle', name=name) for name in tutelles]
print(nodes_tutelles)
print(len(nodes_tutelles))
