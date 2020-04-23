
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from bigload import views

urlpatterns = [
    path('trash/', views.TrashList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
