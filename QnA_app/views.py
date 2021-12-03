from django.shortcuts import *

from python_engine.src.core import get_answer_with_timestamp
from python_engine.src.utils import get_video_id


# Create your views here.
def home(request):
    URL = request.GET.get("URL")
    print("URL=", URL)
    answer = None
    question = request.POST.get("ques")
    video_id = get_video_id(URL)
    timestamp, context = 0, {"turl": "https://www.youtube.com/embed/" + "HcqpanDadyQ"}
    if URL and question:
        # timestamp, answer = get_answer_with_timestamp(URL, question)
        timestamp, answer = 32, "returned answer"
        print("*" * 32, answer, "*" * 32)
        print("Answer:", answer, "Question:", question)

        Turl = (
            "https://www.youtube.com/embed/"
            + video_id
            + f"{URL}?start={timestamp}&autoplay=1"
        )
        context = {"answer": answer, "turl": Turl}

    return render(request, "home.html", context)
