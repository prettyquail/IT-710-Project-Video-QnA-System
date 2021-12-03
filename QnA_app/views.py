from django.shortcuts import *
import json

from python_engine.src import (
    get_video_id,
)


def home(request):
    URL = request.GET.get("URL")
    print("URL=", URL)
    answer = None
    question = request.POST.get("ques")
    video_id = "HcqpanDadyQ" if not URL else get_video_id(URL)
    timestamp, context = 0, {"turl": "https://www.youtube.com/embed/" + "HcqpanDadyQ"}
    if URL and question:
        # timestamp, answer = get_answer_with_timestamp(URL, question)
        timestamp, answer = 32, "returned answer"
        print("*" * 32, answer, "*" * 32)
        print("Answer:", answer, "Question:", question)

        Turl = (
            "https://www.youtube.com/embed/"
            + video_id
            + f"?start={timestamp}&autoplay=1"
        )
        context = {"answer": answer, "turl": Turl}
    elif URL:

        Turl = "https://www.youtube.com/embed/" + get_video_id(URL)
        context = {"answer": answer, "turl": Turl}
    elif question:
        timestamp, answer = 32, "returned answer"
        Turl = (
            "https://www.youtube.com/embed/"
            + "HcqpanDadyQ"
            + f"?start={timestamp}&autoplay=1"
        )
        context = {"answer": answer, "turl": Turl}
    else:
        print("You're fucked!!")

    return render(request, "home.html", context)
