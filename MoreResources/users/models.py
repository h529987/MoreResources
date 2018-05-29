from django.db import models

class normal_user(models.Model):
	user_id = models.IntField()
	user_name = models.CharField(max_length = 64)
	user_passwd = models.CharField(max_length = 32)
	point = models.IntField()
	type = models.CharField(max_length = 16)
	image = models.BlobField()
	introduction = models.CharField(max_length = 100)