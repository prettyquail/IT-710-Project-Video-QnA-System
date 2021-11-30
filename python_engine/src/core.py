import torch
from typing import List, Tuple
from .utils import get_transcript_yt, search_transcript, vtt_to_corpus, clean_text
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline

tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
model = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")
question_answerer = pipeline("question-answering", model=model, tokenizer=tokenizer)


def get_batched_corpus(vtt_path: str, batch_size: int) -> List[str]:
    corpus = clean_text(vtt_to_corpus(vtt_path))
    corpus_words = corpus.split()
    corpus_len = len(corpus_words)
    corpus_batches = [
        " ".join(corpus[idx : idx + batch_size])
        for idx in range(0, corpus_len, batch_size)
    ]
    return corpus_batches


def get_answer_with_timestamp(url: str, question: str) -> Tuple[str, int]:
    with open("subs.vtt", "w+") as subs:
        subs.write(get_transcript_yt(url)["subtitles"])
    corpus_batches = get_batched_corpus("subs.vtt", 512)
    answers = list()
    for batch in corpus_batches:
        answers.append(question_answerer(question=question, context=batch))
    print(answers)
    best_answer = sorted(answers, key=lambda d: d["score"], reverse=True)[0]["answer"]
    print("best answer:", best_answer)
    best_answer_ts = search_transcript(best_answer, "subs.vtt")
    print("best_answer_ts", best_answer_ts)
    return best_answer, best_answer_ts[0]
