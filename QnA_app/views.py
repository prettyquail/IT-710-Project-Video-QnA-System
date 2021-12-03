import json
from django.shortcuts import *
from python_engine.src import get_video_id, get_answer_with_timestamp


def home(request):
    URL = request.GET.get("URL")
    print("URL=", URL)
    answer = None
    question = request.POST.get("ques")
    video_id = "HcqpanDadyQ" if not URL else get_video_id(URL)
    timestamp, context = 0, {"turl": "https://www.youtube.com/embed/" + "HcqpanDadyQ"}
    if URL and question:
        answer, timestamp = get_answer_with_timestamp(URL, question)
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
        answer, timestamp = get_answer_with_timestamp(
            "https://www.youtube.com/watch?v=" + "HcqpanDadyQ", question
        )
        Turl = (
            "https://www.youtube.com/embed/"
            + "HcqpanDadyQ"
            + f"?start={timestamp}&autoplay=1"
        )
        context = {"answer": answer, "turl": Turl}
    else:
        print("You're fucked!!")

    return render(request, "home.html", context)
