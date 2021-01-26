from django.urls import path, include
from qpoll import views as qv
from django.views.decorators.http import require_POST
# from django.conf import settings
# from django.conf.urls.static import static

app_name = 'qpoll'
urlpatterns = [
	path('',qv.IndexQuestionView.as_view(), name='qpoll'),
	path('detail/<int:pk>/',qv.QuestionDetailView.as_view(), name='detail'),
	path('vote/<int:ans_id>/',qv.vote, name='vote'),
	path('result/<int:pk>/',qv.ResultView.as_view(),name='result'),
	path('chart/<int:qust_id>/',qv.chart_data,name='chart'),
	path('my_form/',require_POST(qv.FormsView.as_view()),name='form'),
	path('edit/<int:output_id>',qv.edit_form_view,name='edit'),
	path('delete/<int:pk>',qv.QuestionDelete.as_view(),name='delete')
]
# ] +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)