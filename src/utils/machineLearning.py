import pandas as pd
from sklearn.base import TransformerMixin

class CategoricalDataEncoder(TransformerMixin):
    '''
    Transformer for categorical data values to one-hot fomat.

    '''
    def __init__(self, dummyNa=True, dropFirst=True):
        self.dropFirst  = dropFirst
        self.dummyNa    = dummyNa
        self.categories = {}

    def fit(self, X, y=None):
        for col in X.columns:
             self.categories[col] = pd.Categorical(X[col]).categories
        return self

    def transform(self, X, y=None):
        for col in X.columns:
            X[col] = pd.Categorical(X[col], categories=self.categories[col])

        result = pd.get_dummies(
            X,
            dummy_na   = self.dummyNa,
            drop_first = self.dropFirst
        )
        self.oneHotAttributeName = result.columns.tolist()
        return result

    def get_feature_names(self):
        return self.oneHotAttributeName
