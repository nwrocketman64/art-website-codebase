from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexPage.as_view(), name="index-page"),
    path("contact", views.ContactPage.as_view(), name="contact-page"),
    path("contact-submitted", views.ContactSubmitPage.as_view(), name="contact-submitted"),
    path("works", views.WorkList.as_view(), name="work-list"),
    path("about", views.AboutPage.as_view(), name="about-page"),
]