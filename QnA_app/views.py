from django.shortcuts import render

# Create your views here.
def home(request):
	URL=request.GET.get('URL')
	print("URL=",URL)

	question=request.GET.get('ques')
	print("question=",question)
	split="O8gwfP8AgsY"
	url="https://www.youtube.com/embed/"+split
	print(url)
	return render(request,'home.html',{"url":url})