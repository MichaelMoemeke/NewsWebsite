from django.urls import path
from . import views
from .views import preferences
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = "main"   


urlpatterns = [
    path("index/", views.homepage, name="homepage"),
    path("about/", views.about_request, name="about"),
    path("politics/", views.politics_request, name="politics"),
    path("covid19/", views.covid19_request, name="covid19"),
    path("trending/", views.trending_request, name="trending"),
    path("internationalStories/", views.internationalStories_request, name="internationalStories"),
    path("sports/", views.sports_request, name="sports"),
    path("feedback/", views.feedback_request, name="feedback"),
    path("independent/", views.independent_request, name="independent"),
    path("UkraineConflict/", views.UkraineConflict_request, name="UkraineConflict"),
    path("register/", views.register_request, name="register"),
    path("customFeed/", views.customFeed_request, name="customFeed"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path("preferences/", views.preferences, name="preferences"),
    path("", views.homepage, name="homepage"),
]

urlpatterns += staticfiles_urlpatterns()