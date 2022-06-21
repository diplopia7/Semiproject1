from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.list, name='board/list.html'),
    path('write/',views.write, name='board/write.html'),
    path('view/',views.view, name='board/view.html'),
]