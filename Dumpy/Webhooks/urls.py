from django.urls import path
from . import views

urlpatterns = [
    path('', views.handle_webhooks, name='webhooks'),
    path('/view-queries',views.queries,name='queries'),
]
