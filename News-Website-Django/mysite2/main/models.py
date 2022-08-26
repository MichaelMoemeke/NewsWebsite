from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Create your models here.
class UserPreferenceForm(models.Model):

	DIFFERENT_CATEGORIES = [
		('politics', 'Politics'),
	    ('covid-19', 'Covid-19'),
	    ('trending', 'Trending'),
	    ('international stories', 'International stories'),
	    ('independent sources', 'Independent Sources'),
	    ('sports', 'Sports'),
		('war in ukraine', 'War in Ukraine'),
	]
	
	title = MultiSelectField(choices = DIFFERENT_CATEGORIES) 
	userStuff = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name="title", null=True)

	def __str__(self):   
		return self.title[0]
	
