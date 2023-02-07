from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView

# Import the needed classes from other files.
from .forms import RequestForm
from .models import Request, Work

# Create your views here.

class IndexPage(TemplateView):
    """ Index Page
    The class returns the index page with the latest product.
    """
    # Set the template.
    template_name = "main_site/index.html"


    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Update and return the context.
        context["title"] = "Home"
        context["path"] = "/home"
        return context


class ContactPage(CreateView):
    """ Contact Page
    The class renders the contact view page based off of the request
    model.
    """
    # Set the template, model, form, and url redirect.
    template_name = "main_site/contact.html"
    model = Request
    form_class = RequestForm
    success_url = "/contact-submitted"


    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Contact Us"
        context["path"] = "/contact"
        return context


class ContactSubmitPage(TemplateView):
    """Contact Submit Page
    The class renders the contact success submit page.
    """
    # Set the template.
    template_name = "main_site/contact-submit.html"


    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Comment/Question Submitted"
        context["path"] = "/contact"
        return context


class WorkList(ListView):
    """ Work List
    The class delivers the full list of works page.
    """
    # Set the template, model, and order by date.
    template_name = "main_site/works.html"
    model = Work
    ordering = ["-date"]
    context_object_name = "works"
    paginate_by = 6


    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Full List of Works of Art"
        context["path"] = "/works"
        return context


class WorkDetails(DetailView):
    """ Work Details
    The class returns the details of each work of art.
    """
    # Set the template and the model.
    template_name = "main_site/work-detail.html"
    model = Work


    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work Details"
        context["path"] = "/works"
        return context


class AboutPage(TemplateView):
    """About Page
    The class delivers the about me page.
    """
    # Set the template.
    template_name = "main_site/about.html"


    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "About the Artist"
        context["path"] = "/about"
        return context