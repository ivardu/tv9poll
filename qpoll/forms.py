from django.forms import ModelForm
from qpoll.models import Question

class QuestionForm(ModelForm):

	class Meta:
		model = Question
		fields = ['question']