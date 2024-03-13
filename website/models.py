from django.db import models

# Create your models here.
class HomePage(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    Title_Text = models.CharField(max_length=2000, help_text='Enter Big Text')
    Subtitle_Text = models.CharField(max_length=1000, help_text='Enter Sub Text')
    Cover_Photo = models.ImageField(upload_to="uploadedMedia/",help_text="Upload Cover Photo To Be Used As Background Of Home Page")
     
    # Methods
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return "Home Page"
class Page(models.Model):
    """A typical class defining a model, derived from the Model class."""
    list_display = ('id', 'Title_Text', 'Category')
    # Fields
    id = models.AutoField(primary_key=True)
    Has_Title = models.BooleanField(default=True)
    Title_Text = models.CharField(max_length=2000, help_text='Title of page (If Applicable)')
    Content = models.CharField(max_length=1000000)
    Category = models.CharField(max_length=1000000, choices=[("about","About"), ("meet_team","Meet The Team"), ("meet_research","Meet The Researchers"), ("research","Researches")], default="about")
     
    # Methods
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return "Page"
