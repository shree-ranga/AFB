import datetime

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

    def validate(self, attrs):
        if (attrs["due_date"] is not None) and (
            attrs["due_date"] < datetime.datetime.now().date()
        ):
            raise serializers.ValidationError(
                "due date must be greater than today's date"
            )
        return attrs
