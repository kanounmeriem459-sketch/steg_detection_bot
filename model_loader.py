def load_my_model():

    class FakeModel:
        def predict(self, x):
            return [[0.85]]

    return FakeModel()