from django.shortcuts import render
from pyqna.models.reading_comprehension.transformer_models import TransformerQnAModel
from python_engine.src import (
    get_transcript_yt,
    vtt_to_corpus,
    search_transcript,
    get_video_id,
)


model = TransformerQnAModel(
    {"model_name": "distilbert-base-uncased-distilled-squad", "pre_trained": True}
)

# Create your views here.
def home(request):
    URL = request.GET.get("URL")
    print("URL=", URL)
    if URL:
        with open("subs.vtt", "w+") as vtt_file:
            vtt_file.write(get_transcript_yt(URL)["subtitles"])
    corpus = vtt_to_corpus("subs.vtt")
    question = request.GET.get("ques")
    print("question=", question)
    if question:
        answer = model.get_answer(corpus, question)
        print("*" * 32, answer, "*" * 32)

    video_id = get_video_id(URL)
    url = "https://www.youtube.com/embed/" + (video_id if video_id else "HcqpanDadyQ")
    print(url)
    return render(request, "home.html", {"url": url})
