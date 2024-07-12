import pytest
import os
import pandas as pd
from ml.model import train_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_model():
    """
    # Checking the model is the RandomForestClassifier.
    """
    sample_x = [[1, 2, 3], [4, 5, 6]]
    sample_y = ['low', 'high']

    model = train_model(sample_x, sample_y)

    assert type(model) == type(RandomForestClassifier())


# TODO: implement the second test. Change the function name and input as needed
def test_data_size():
    """
    Checking that data is sliced into an appropriate size for testing.
    """
    data_path = './data/census.csv'
    data = pd.read_csv(data_path)
    train, test = train_test_split(data, test_size = 0.2)
    assert len(test) >= 2000


# TODO: implement the third test. Change the function name and input as needed
def test_features():
    """
    Checking that all features are present.
    """
    data_path = './data/census.csv'
    data = pd.read_csv(data_path)

    features = {
        'age', 'workclass', 'fnlgt', 'education', 'education-num', 'marital-status', 
        'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 
        'hours-per-week', 'native-country', 'salary'
    }

    assert set(data.columns) == features
