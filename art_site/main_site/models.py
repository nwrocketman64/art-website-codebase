from datetime import datetime, timezone, timedelta
from django.db import models
from django.utils.text import slugify

# Create your models here.


class Request(models.Model):
    """ Request
    The class defines how request from the contact form are saved.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    comment = models.TextField()
    sent_time = models.DateTimeField(editable=False)


    # The function defines how each request appears in admin.
    def __str__(self):
        # Create timezone for Arizona.
        sgtTimeDelta = timedelta(hours=-7)
        sgtTZObject = timezone(sgtTimeDelta, name="SGT")

        # Return the string of the object.
        return f"{self.first_name} {self.last_name} on {self.sent_time.astimezone(sgtTZObject).strftime('%A, %b %d, %Y - %I:%M %p')}"


    # The function saves sent_time as the current time the request was
    # saved.
    def save(self, *args, **kwargs):
        # Create datetime object and set it to now.
        current_time = datetime.now()

        # Set sent time to the current time.
        self.sent_time = current_time

        # Save everything else.
        super().save(*args, **kwargs)