from django.urls import path

from .views import runplan

# Пространство имен
app_name = 'run_plan'

urlpatterns = [
    path('', runplan, name='runplan'),
]
