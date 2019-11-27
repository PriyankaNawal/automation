import utilities.read_json as rj
import os


def test_data(attribute):
    test_data_path = os.path.abspath("./testdata/data.json")
    test_data_json_file = rj.read_json(test_data_path)
    return test_data_json_file[attribute]