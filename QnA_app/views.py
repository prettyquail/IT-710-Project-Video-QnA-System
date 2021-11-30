from django.shortcuts import *

from python_engine.src.core import get_answer_with_timestamp
from python_engine.src.utils import get_video_id


# Create your views here.
def home(request):
    URL = request.GET.get("URL")
    print("URL=", URL)
    answer = None
    question = request.POST.get("ques")
    if URL:
        timestamp, answer = get_answer_with_timestamp(URL, question)
        print("*" * 32, answer, "*" * 32)
        print("Answer:", answer, "Question:", question)
    video_id = get_video_id(URL)
    url = "https://www.youtube.com/embed/" + (video_id if video_id else "HcqpanDadyQ")
    print(url)
    return render(request, "home.html", {"url": url})
