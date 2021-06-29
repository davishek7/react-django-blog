from django.db import models
from django.conf import settings
from django.utils import timezone


class Category(models.Model):
	name = models.CharField(max_length = 100,blank = True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'categories'


class Post(models.Model):

	class PostObjects(models.Manager):
		def get_queryset(self):
			return super().get_queryset().filter(status='published')

	options = (
		('draft','Draft'),
		('published','Published'),
		)

	title = models.CharField(max_length = 255,blank = True)
	slug = models.SlugField(max_length = 255,unique_for_date='published')
	content = models.TextField(blank = True)
	published = models.DateTimeField(default = timezone.now)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE,blank = True)
	category = models.ForeignKey(Category,on_delete = models.PROTECT,blank = True)
	status = models.CharField(max_length=10,choices=options,default='draft')
	objects = models.Manager()
	postobjects = PostObjects()

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-published']