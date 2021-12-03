import allennlp_models
from allennlp.predictors.predictor import Predictor

predictor = Predictor.from_path("hf://lysandre/bidaf-elmo-model-2020.03.19")
predictor_input = {
    "passage": "My name is Wolfgang and I live in Berlin",
    "question": "Where do I live?",
}
predictions = predictor.predict_json(predictor_input)
start, end = predictions['best_span']
print(predictions["passage_tokens"][start:end+1])
