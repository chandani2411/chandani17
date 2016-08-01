from django.contrib.auth.models import User

from models import Reply,Comment

from rest_framework import serializers




class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment

        # fields = '__all__'

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        # fields = '__all__'
