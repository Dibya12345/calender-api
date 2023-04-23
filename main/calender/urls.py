from django.urls import path

from . import views

urlpatterns = [
    path("v1", views.index, name="index"),
    path('v1/calendar/init/', views.GoogleCalendarInitView, name='google_permission'),
    path('v1/calendar/redirect/', views.GoogleCalendarRedirectView, name='google_redirect')
]