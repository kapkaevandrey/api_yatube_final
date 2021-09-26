from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

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
    user = SlugRelatedField(slug_field="username", read_only=True,
                            default=serializers.CurrentUserDefault())
    following = SlugRelatedField(slug_field="username",
                                 queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ("user", "following")
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=("following", "user")
            )
        ]

    def validate(self, attrs):
        user = self.context["request"].user
        if attrs['following'] == user:
            raise serializers.ValidationError(
                'Не стоит подписываться на самого себя!')
        return attrs
