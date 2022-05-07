import requests 
import streamlit as st


url = "https://api.inaturalist.org/v1/"

def get_results(name, limit=10):
    # url = f"https://api.inaturalist.org/v1/search?q={name}&sources=taxa&per_page={limit}"
    url = f"https://api.inaturalist.org/v1/search?q={name}&per_page={limit}"
    r = requests.get(url)
    data = r.json()
    return data

def get_default_image(data, limit=10):
    if data.get('results'):
        # item = data['results'][0]['record']
        results = []
        for item in data['results']:
            item = item['record']
            if item.get('default_photo', ''):
                results.append(item['default_photo']['medium_url'])
            else:
                st.write("No default photo")
            if len(results) == limit:
                break
        return results 

def get_taxon_images(data, limit=10):
    if data.get('results'):
        # item = data['results'][0]['record']
        results = []
        for item in data['results']:
            item = item['record']
            if item.get("taxon_photos"):
                for tp in item['taxon_photos']:
                    results.append(tp['photo']['medium_url'])
                    # try:
                        # results.append(tp['large_url'])
                    # except:
                if len(results) >= limit:
                    break
    return results

def get_taxon_images_b(data, limit=10):
    results = []
    item = data['record']
    if item.get("taxon_photos"):
        for tp in item['taxon_photos']:
            results.append(tp['photo']['medium_url'])
            # try:
                # results.append(tp['large_url'])
            # except:
            if len(results) >= limit:
                break
    return results