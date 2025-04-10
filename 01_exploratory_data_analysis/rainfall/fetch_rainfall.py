import requests, os, tempfile
import pandas as pd
import numpy as np

name_convert = {'Bosnia and Herzegovina': 'Bosnia-Herzegovinia',
                'Cape Verde': 'Cape_Verde_Isl',
                'Central African Republic': 'Central_African_Rep',
                'Czechia': 'Czech Republic',
                'Democratic Republic of Congo': 'DR_Congo',
                'Eswatini': 'Swaziland',
                'Faeroe Islands': 'Faeroes',
                'Palau': 'Palau_Isl',
                'North Macedonia': 'Macedonia',
                'Marshall Islands': 'Marshall_Isl',
                'Palau': 'Palau_Isl',
                'Saint Kitts and Nevis': 'St_Kitts_and_Nevis',
                'Saint Lucia': 'St_Lucia',
                'Saint Vincent and the Grenadines': 'St_Vincent',
                'Solomon Islands': 'Solomon_Isl',
                'United States': 'USA',
                "Cote d'Ivoire": 'Ivory_Coast'
                }

def fetch_rainfall(country_list, iso_codes):
    """
    Horrible quick fix, (TODO) refactor.
    """
    url = 'https://crudata.uea.ac.uk/cru/data/hrg/cru_ts_4.08/crucy.2407032054.v4.08/countries/tmp/crucy.v4.08.1901.2023.'
    suffix = '.tmp.per'

    if len(country_list) != len(iso_codes):
        raise ValueError('The length of the provided country names list does not match the length of iso codes.')

    temps_to_add = pd.DataFrame()
    for ic, country in enumerate(country_list):
        if country in name_convert:
            ctr = name_convert[country]
        else:
            ctr = country
        ctr = ctr.replace(' ', '_')
        full_url = f'{url}{ctr}{suffix}'
        try:
            response = requests.get(full_url)
            response.raise_for_status()

            year = []
            temp = []

            with tempfile.NamedTemporaryFile(delete_on_close=False) as fp:
                for chunk in response.iter_content(chunk_size=8192):
                    fp.write(chunk)
                fp.close()

                with open(fp.name, mode='rb') as f:
                    for i, line in enumerate(f):
                        if i > 3:
                            ls = line.split()
                            year.append(int(ls[0]))
                            temp.append(float(ls[-1]))

            to_add = pd.DataFrame({'ISO3_code': [iso_codes[ic]]*len(year),
                                   'Year': year,
                                   'mean_temp': temp
                                   })
            temps_to_add = pd.concat([temps_to_add, to_add])
        except requests.exceptions.RequestException as e:
            print(f"Error downloading file: {e}")
            print(f'Warning: could not find {country}, skipping.')
            print(full_url)
            continue
    return temps_to_add