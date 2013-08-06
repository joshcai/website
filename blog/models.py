from django.db import models

# Create your models here.

class Tag(models.Model):
	descript = models.CharField(max_length=120)
	def __unicode__(self):
		return self.descript


class Post(models.Model):
	subject = models.CharField(max_length=120)
	content = models.TextField()
	content_rendered = models.TextField(default="")
	date = models.DateTimeField('date created')
	date_str = models.CharField(max_length=120)
	deleted = models.BooleanField(default=False)
	tags = models.ManyToManyField(Tag)
	def __unicode__(self):
		return self.subject
