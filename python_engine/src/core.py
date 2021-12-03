import uuid
import allennlp_models
from functools import lru_cache
from typing import List, Tuple
from allennlp.predictors.predictor import Predictor
from .utils import get_transcript_yt, search_transcript, vtt_to_corpus


predictor = Predictor.from_path("hf://lysandre/bidaf-elmo-model-2020.03.19")


@lru_cache(maxsize=100)
def get_answer_with_timestamp(url: str, question: str) -> Tuple[str, int]:
    with open("subs.vtt", "w+") as subs:
        subs.write(get_transcript_yt(url)["subtitles"])
    corpus = vtt_to_corpus("subs.vtt")
    predictor_input = {
        "passage": corpus,
        "question": question,
    }
    predictions = predictor.predict_json(predictor_input)
    start, end = predictions["best_span"]
    answer = " ".join(predictions["passage_tokens"][start : end + 1])
    print("Unbatched Answer:", answer)
    best_answer_ts = search_transcript(answer, "subs.vtt")
    print("Unbatched best_answer_ts", best_answer_ts)
    return answer, best_answer_ts[0]
