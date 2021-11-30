from typing import List, Tuple
from functools import lru_cache
from .utils import get_transcript_yt, search_transcript, vtt_to_corpus
from pyqna.models.reading_comprehension.transformer_models import TransformerQnAModel


model = TransformerQnAModel(
    {"model_name": "distilbert-base-uncased-distilled-squad", "pre_trained": True}
)


@lru_cache(maxsize=100)
def get_batched_corpus(vtt_path: str, batch_size: int) -> List[str]:
    corpus = vtt_to_corpus(vtt_path)
    corpus_words = corpus.split()
    corpus_len = len(corpus_words)
    corpus_batches = [
        " ".join(corpus[idx : idx + batch_size])
        for idx in range(0, corpus_len, batch_size)
    ]
    return corpus_batches


def get_answer_with_timestamp(url: str, question: str) -> Tuple[str]:
    with open("subs.vtt", "w+") as subs:
        subs.write(get_transcript_yt(url)["subtitles"])
    corpus_batches = get_batched_corpus("subs.vtt", 512)
    answers = list()
    for batch in corpus_batches:
        answers.append(model.get_answer(batch, question))
    best_answer = sorted(answers, key=lambda d: d["score"], reverse=True)[0]["answer"]
    print(best_answer)
    best_answer_ts = search_transcript(best_answer, "subs.vtt")
    return best_answer_ts[0], best_answer
