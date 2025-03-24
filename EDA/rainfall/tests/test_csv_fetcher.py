import sys, os
import tempfile
import shutil
import pytest, requests

sys.path.insert(0, '.')
sys.path.insert(1, '..')

from utils import CsvFetcher

class TestCsvFetcher:
    def test_init(self):
        # TODO: have checks in constructor to check if string a URL?
        fetcher = CsvFetcher('test')

    def test_fetch(self):
        fetcher = CsvFetcher('https://cadmus.eui.eu/bitstream/handle/1814/64606/Historical_Index_of_Ethnic_Fractionalisation_Dataset.csv?sequence=3&isAllowed=y')
        
        temp_dir = tempfile.mkdtemp()
        new_folder = 'data'
        new_path = os.path.join(temp_dir, new_folder)
        df = fetcher.fetch(file_name='test.csv', extract_to=new_path, delete_file=False)

        assert os.path.exists(new_path)

        path_to_file = os.path.join(new_path, 'test.csv')
        assert os.path.exists(path_to_file)

        shutil.rmtree(temp_dir)

        assert len(df) != 0

    def test_fetch_fail(self):
        fetcher = CsvFetcher('blah')

        with pytest.raises(requests.exceptions.RequestException):
            fetcher.fetch()