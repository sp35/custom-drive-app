from django.db import models
from django.contrib.auth.models import User


class Upload(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='file_user')
	file = models.FileField(upload_to= '')

	def __str__(self):
		return self.user.username