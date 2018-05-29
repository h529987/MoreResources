from django.db import models

class normal_user(models.Model):
	user_id = models.IntField(primary_key = True)
	user_name = models.CharField(max_length = 64)
	user_passwd = models.CharField(max_length = 32)
	point = models.IntField(null = True)
	type = models.CharField(max_length = 16)
	image = models.BlobField(null = True)
	introduction = models.CharField(max_length = 100, null = True)