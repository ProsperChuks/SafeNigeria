from django.urls import path

from core import views

app_name = 'core'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('news/', views.NewFeedView.as_view(), name='news'),
    path('cities/', views.CitiesView.as_view(), name='cities'),
    path('report/', views.ReportPageView.as_view(), name='report'),
]