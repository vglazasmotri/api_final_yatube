from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Group, Comment, Post, Follow, User


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group."""
    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post."""
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment."""
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Follow."""
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )

    class Meta:
        model = Follow
        fields = ('id', 'user', 'following')
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Вы уже подписывались на этого автора.',
            ),
        ]

    def validate(self, data):
        """Если совпадают имя пользователя и автора выдает ошибку."""
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!')
        return data
