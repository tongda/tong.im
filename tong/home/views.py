from django.http import HttpResponse

def index(request):
	return HttpResponse('Hello, I\'m Tong Da')
