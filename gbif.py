import requests

def get_species():
    return ["GBIF Option 1", "GBIF Option 2", "GBIF Option 3"]


def api_suggest(name):
    url = "https://api.gbif.org/v1/species/suggest?q={}".format(name)
    r = requests.get(url)
    data = r.json()
    return data


def get_s_names(data):
    return [d["scientificName"] for d in data]


def suggest(name):
    return api_suggest(name)


def get_item(key):
    url = "https://api.gbif.org/v1/species/{}".format(key)
    r = requests.get(url)
    data = r.json()
    return data

def get_ny_species(ids):
    a_d = []
    for id in ids:
        r = requests.get(f'https://api.gbif.org/v1/occurrence/{id}')
        data = r.json()
        a_d.append(data)
    return a_d


def get_media(key):
    # url = "https://api.gbif.org/v1/species/{}/media".format(key)
    url = "https://api.gbif.org/v1/species/{}/media".format(key)
    r = requests.get(url)
    data = r.json()
    return data