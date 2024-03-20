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
class Social(models.Model):
    """A typical class defining a model, derived from the Model class."""
    # Fields
    id = models.AutoField(primary_key=True)
    Social_Media = models.CharField(max_length=1000000, choices=[("fa-facebook","Facebook"), ("fa-youtube","Youtube"), ("fa-instagram","Instagram"), ("fa-twitter","Twitter"), ("fa-linkedin","Linkedin")], default="fa-instagram")
    Social_Media_Link = models.CharField(max_length=2000, help_text='Link to social media profile')

    # Methods
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return "Page"
class Contact(models.Model):
    """A typical class defining a model, derived from the Model class."""
    # Fields
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=2000)
    Email = models.EmailField(max_length=2000)
    Phone_Number = models.CharField(max_length=20, help_text='Phone Number in this format: +971501234567 or type N/A if you don\'t want to show number')
    Position = models.CharField(max_length=2000, choices=[("Head", "Head"),("Junior Head", "Junior Head")])
    Picture = models.ImageField(max_length=2000, upload_to='uploadedMedia', default='/static/images/placeholder.webp')

    # Methods
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return "Page"
