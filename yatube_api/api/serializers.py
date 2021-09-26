from rest_framework import serializers
from rest_framework import status
from rest_framework.relations import SlugRelatedField
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "title", "slug", "description"]


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field="username", read_only=True)
    following = SlugRelatedField(slug_field="username",
                                 read_only=True)

    class Meta:
        model = Follow
        fields = ["user", "following"]
        required_fields = "following"

    def create(self, validated_data):
        print(validated_data)
        print(self.initial_data)
        super().create(validated_data)
