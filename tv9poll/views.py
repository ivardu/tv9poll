from django.http import HttpResponse

def home(request):
	return HttpResponse('Welcome to the Tv9 Questionnaire poll page')
