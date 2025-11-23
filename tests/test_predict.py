import pytest
import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.main import predict


def test_predict_negatif():
    assert predict(1)['label'] == 'negatif'
    assert predict(2)['label'] == 'negatif'




def test_predict_neutre():
    assert predict(3)['label'] == 'neutre'




def test_predict_positif():
    assert predict(4)['label'] == 'positif'
    assert predict(5)['label'] == 'positif'