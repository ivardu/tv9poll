from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, DeleteView
from qpoll.models import Question, Answer
from django.urls import reverse, reverse_lazy
from qpoll.forms import QuestionForm
from django.views.decorators.http import require_POST
import json
# Create your views here.


class IndexQuestionView(ListView):
	model = Question
	template_name = 'qpoll/index.html'
	context_object_name = 'question'

	def get_context_data(self, **kwargs):
		context = super(IndexQuestionView, self).get_context_data(**kwargs)
		context['form'] = QuestionForm
		# context['count'] = 0
		# context['question'] = dict(zip(list(map(str, Question.objects.all())),[val for val in range(1, len(Question.objects.all()))]))
		return context

# @require_POST
class FormsView(FormView):
	form_class = QuestionForm
	success_url = reverse_lazy('qpoll:qpoll')

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)


class ResultView(DetailView):
	model = Question
	template_name = 'qpoll/result.html'
	context_object_name = 'quest'

class QuestionDelete(DeleteView):
	model = Question
	template_name = 'qpoll/delete.html'
	success_url = reverse_lazy('qpoll:qpoll')


class QuestionDetailView(DetailView):
	model = Question
	template_name='qpoll/detail.html'
	context_object_name = 'output'

	
	def get_object(self):
		output = Question.objects.get(pk=self.kwargs['pk'])
		if bool(output.answer_set.all()) == False:
			output.answer_set.create()
		return output
		


def vote(request, ans_id):
	output = Question.objects.get(pk=ans_id)
	try:
		var = Answer.objects.get(question_id=output.id)
		dit = request.POST
		if ('Yes' not in dit.values()) and ('No' not in dit.values()):
			raise Exception('No Choice was selected')
	except Exception as e:
		# return render(request,'qpoll/detail.html',{'question':output,'context':e})
		return render(request,'qpoll/detail.html',{'output':output,'error_message':e})
		# return HttpResponse(e)
	else:
		if request.method == 'POST':
			if 'Yes' in dit.values():	
				var.yes += 1
				var.save()
			elif 'No' in dit.values():
				var.no += 1
				var.save()
		return HttpResponseRedirect(reverse('qpoll:result', args=(var.question_id,)))
		# return HttpResponse(dit)


def edit_form_view(request, output_id):
	question = Question.objects.get(pk=output_id)
	if request.method == 'POST':
		form = QuestionForm(request.POST, instance=question)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('qpoll:detail',args=(question.id,)))
	else:
		form = QuestionForm(instance=Question.objects.get(pk=output_id))

	return render(request,'qpoll/edit.html',{'form':form,'output':question})


def chart_data(request, qust_id):
	 answer = Answer.objects.get(question_id=qust_id)
	 ans_yes, ans_no = [], []
	 ans_yes.append((answer.yes)*100/(answer.yes+answer.no))
	 ans_no.append((answer.no)*100/(answer.yes+answer.no))
	 chart = {
	 	'chart':{'type':'column'},
	 	'title':{'text':'Tv9 Questionnarie Poll Graph'},
	 	'xAxis':{
	 		'categories':['Poll value']
	 	},
	 	'yAxis':{
	 		'title':{
	 			'text':'Percentage (%)'
	 		}
	 	},
	 	'series':[
	 		{'name':'Yes','data':ans_yes},
	 		{'name':'No','data':ans_no},
	 	]
	 }

	 return JsonResponse(chart)
