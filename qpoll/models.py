from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Question(models.Model):
	question = models.CharField(max_length=150)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.question

	def get_question_id(self):
		return self.id
	get_question_id.short_description = 'Question Id'
	get_question_id.admin_order_field = 'id'

	# def get_absolute_url(self):
	# 	return reverse('qpoll',kwargs={pk:'self.pk'})

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	yes = models.IntegerField(default=0)
	no = models.IntegerField(default=0)

	def __str__(self):
		return self.question.question