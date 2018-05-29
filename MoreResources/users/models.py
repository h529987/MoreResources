from django.db import models

class normal_user(models.Model):
	user_id = models.IntegerField(
		primary_key = True,
		)
	user_name = models.CharField(
		max_length = 64,
		)
	user_passwd = models.CharField(
		max_length = 32,
		)
	point = models.IntegerField(
		null = True,
		)
	type = models.CharField(
		max_length = 16,
		)
	image = models.ImageField(
		null = True,
		)
	introduction = models.CharField(
		max_length = 100, 
		null = True,)

class  expert(models.Model):
	expert_id = models.ForeignKey(
		'normal_user', 
		on_delete = models.CASCADE,
		)
	contact = models.CharField(
		max_length = 32
		)

class administrator(models.Model):
	administrator_id = models.ForeignKey(
		'normal_user',
		on_delete = models.CASCADE,
		)