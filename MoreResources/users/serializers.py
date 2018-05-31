from rest_framework import serializers
from users.models import normal_user, expert, administrator

class NormalUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = normal_user
		fields = '__all__'

class ExpertSerializer(serializers.ModelSerializer):
	class Meta:
		model = expert
		fields = '__all__'

class AdministratorSerializer(serializers.ModelSerializer):
	class Meta:
		model = administrator
		fields = '__all__'