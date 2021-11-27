from django.shortcuts import render
from pyqna.models.reading_comprehension.transformer_models import TransformerQnAModel
from python_engine.src import (
    get_transcript_yt,
    vtt_to_corpus,
    search_transcript,
    get_video_id,
)

# Create your views here.
def home(request):
    URL = request.GET.get("URL")
    print("URL=", URL)
    if URL:
        with open("subs.vtt", "w+") as vtt_file:
            vtt_file.write(get_transcript_yt(URL)["subtitles"])
    question = request.GET.get("ques")
    print("question=", question)
    video_id = get_video_id(URL)
    url = "https://www.youtube.com/embed/" + (video_id if video_id else "HcqpanDadyQ")
    print(url)
    return render(request, "home.html", {"url": url})
