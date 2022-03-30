from django.db import models
from django.urls import reverse


class Contact(models.Model):
	name = models.CharField(max_length=50)
	fone = models.CharField(max_length=20)
	email = models.EmailField(max_length=100)
	image = models.ImageField(null=True, blank=True, upload_to='images')
	info = models.TextField(blank=True, null=True, max_length=200)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('detail', kwargs={'id': self.id})
