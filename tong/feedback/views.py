from django.shortcuts import render

from models import Feedback

def index(request):
	return render(request, "feedback/index.html", {"feedbacks": Feedback.objects.all()})
