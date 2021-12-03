from django.shortcuts import *
import json
# from pyqna.models.reading_comprehension.transformer_models import TransformerQnAModel
# from python_engine.src import (
#     get_transcript_yt,
#     vtt_to_corpus,
#     search_transcript,
#     get_video_id,
# )

#
# model = TransformerQnAModel(
#     {"model_name": "distilbert-base-uncased-distilled-squad", "pre_trained": True}
# )
#



def home(request):
    URL = request.GET.get("URL")
    print("URL=", URL)
    answer = None
    question = request.POST.get("ques")
    video_id = "HcqpanDadyQ"
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

    return render(request, "home.html", context)






# Create your views here.
# def home(request):
#     URL = request.GET.get("URL")
#     print("URL=", URL)
#     answer="Machine learning is the study of computer algorithms that can improve automatically through experience and by the use of data. It is seen as a part of artificial intelligence."
#     question = request.POST.get("ques")
#     # if URL:
#     #     with open("subs.vtt", "w+") as vtt_file:
#     #         vtt_file.write(get_transcript_yt(URL)["subtitles"])
#     #         corpus = vtt_to_corpus("subs.vtt")
#     #
#     #         answer = model.get_answer(corpus, question)
#     #         print("*" * 32, answer, "*" * 32)
#     print("Answer:",answer,"Question:",question)
#     # video_id = get_video_id(URL)
#     # url = "https://www.youtube.com/embed/" + (video_id if video_id else "HcqpanDadyQ")
#     # print(url)
#
#     # timestamps = search_transcript(answer, "subs.vtt")
#     # url += f"?t={timestamps[0]}"
#
#     context={}
#     URL = "https://www.youtube.com/embed/HcqpanDadyQ"
#     Turl = "https://www.youtube.com/embed/HcqpanDadyQ?start=45&autoplay=1"
#     if URL and question:
#         context = {"url":URL,"answer":answer,"turl":Turl}
#     return render(request, "home.html", context)


