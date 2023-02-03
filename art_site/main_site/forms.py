from django import forms

from .models import Request


class RequestForm(forms.ModelForm):
    """ Request Form
    The class defines the form that appears in the contact page.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'

    class Meta:
        # Define the model the form is based off of.
        model = Request

        # List the fields that should appear in the form.
        # Include all the fields except for sent time.
        fields = [
            "first_name",
            "last_name",
            "email",
            "comment",
        ]

        # Define the labels for the form fields.
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email",
            "comment": "Comments / Questions",
        }

        # Define some key error messages for each form field.
        error_messages = {
            "first_name": {
                "required": "Your first name must not be empty",
                "max_length": "Please enter a shorter first name",
            },
            "last_name": {
                "required": "Your last name must not be empty",
                "max_length": "Please enter a shorter last name",
            },
            "email": {
                "required": "Your email is required",
                "max_length": "Please enter a shorter email",
            },
            "comment": {
                "required": "A comment or question is required",
            },
        }