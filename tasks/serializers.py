from django.contrib.auth import get_user_model

from rest_framework import serializers

from tasks.models import Task

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]
        read_only_fields = ["id"]


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["id"]
