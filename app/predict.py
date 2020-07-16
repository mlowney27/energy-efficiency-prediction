import pickle
config = {"model": "randomforest.p"}
with open(config['model'], "rb") as f:
    model = pickle.load(f)

FEATURES = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8']

def validate_input(json_input):
    """
    Ensure that all features exist in json request
    """
    try:
        for f in FEATURES:
            float(json_input[f])
    except Exception:
        return False
    return True


def predict_building(json_input):
    input_features = []
    for f in FEATURES:
        input_features.append(float(json_input[f]))
    input_vector = [input_features]
    return model.predict(input_vector)

