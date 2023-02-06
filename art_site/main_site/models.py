from datetime import datetime, timezone, timedelta
from django.db import models
from django.utils.text import slugify
from PIL import Image as PILImage, ImageOps

# Create your models here.


class Work(models.Model):
    """ Work
    The class defines how works are saved.
    """
    title = models.CharField(max_length=50)
    description = models.TextField()
    lenght = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    date = models.DateTimeField(blank=True, null=True, editable=False)
    image = models.ImageField(upload_to="images")
    external_url = models.URLField(max_length=200, blank=True, null=True)
    slug = models.SlugField(default="", blank=True, editable=False,
                            null=False, db_index=True, unique=True)
    

    # The function defines how each work of art appears in the admin.
    def __str__(self):
        # Create the timezone for Arizona.
        sgtTimeDelta = timedelta(hours=-7)
        sgtTZObject = timezone(sgtTimeDelta, name="SGT")

        # Return the string of the object.
        return f"{self.title} - Last Updated: {self.date.astimezone(sgtTZObject).strftime('%A, %b %d, %Y - %I:%M %p')}"

    
    # The function creates the slug and sets the last update.
    def save(self, *args, **kwargs):
        # Create the slug for the entry.
        self.slug = slugify(self.title)

        # Create datetime object and set it to now.
        current_time = datetime.now()

        # Set sent time to the current time.
        self.date = current_time

        # Save everything else.
        super().save(*args, **kwargs)

        # Set the base width and height for the thumbnail of the image.
        base_width = 700
        base_height = 700

        # Grab the image that was just saved.
        img_data = PILImage.open(self.image.path)

        # Use exif_transpose to maintain image EXIF metadate
        img = ImageOps.exif_transpose(img_data)

        # Resize the image that was just save and then save the image.
        img.thumbnail((base_width, base_height), PILImage.LANCZOS)
        img.save(self.image.path)


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