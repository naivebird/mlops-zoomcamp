import os
from datetime import datetime

import pandas as pd
from deepdiff import DeepDiff

import batch

def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)

def test_prepare_data():
    data = [
    (None, None, dt(1, 1), dt(1, 10)),
    (1, 1, dt(1, 2), dt(1, 10)),
    (1, None, dt(1, 2, 0), dt(1, 2, 59)),
    (3, 4, dt(1, 2, 0), dt(2, 2, 1)),      
]

    columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    df = pd.DataFrame(data, columns=columns)

    batch.save_data(df, batch.get_input_path(2023, 1))

    batch.main(2023, 1)

    data = batch.read_data(batch.get_output_path(2023, 1), categorical=['PULocationID', 'DOLocationID'])

    expected_records = [{'ride_id': '2023/01_0', 'predicted_duration': 23.19714924577506}, {'ride_id': '2023/01_1', 'predicted_duration': 13.08010120625567}]

    diff = DeepDiff(data.to_dict("records"), expected_records, significant_digits=1)

    print(f'diff={diff}')

    assert 'type_changes' not in diff
    assert 'values_changed' not in diff
    
if __name__ == "__main__":
    test_prepare_data()