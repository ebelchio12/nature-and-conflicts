import requests, os
import pandas as pd

class CsvFetcher:
    def __init__(self, url):
        self.url = url
        
    def fetch(self, file_name='temp.csv', extract_to='data', delete_file=True):
        """
        TODO: refactor (because it rewrites a lot of the functionality of the Rainfall
        fetcher).
        """
        if extract_to.endswith('/'):
            extract_to = extract_to[:-1]

        if not os.path.isdir(extract_to):
            os.mkdir(extract_to)

        # TODO: more detailed error handling (e.g. check url first)
        try:
            response = requests.get(self.url)
            response.raise_for_status()

            with open(f"{extract_to}/{file_name}", 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            data_frame = pd.read_csv(f"{extract_to}/{file_name}")

            if delete_file:
                os.remove(f"{extract_to}/{file_name}")
                if len(os.listdir(extract_to)) == 0:
                    os.rmdir(extract_to)
            return data_frame
        except requests.exceptions.RequestException as e:
            print("Error downloading file: {e}")
            raise e
        