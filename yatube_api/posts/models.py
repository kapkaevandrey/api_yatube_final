from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return f" Group title <{self.title}> id <{self.id}>"

    class Meta:
        ordering = ['title']


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации',
                                    auto_now_add=True,
                                    db_index=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name="posts", blank=True, null=True
    )

    def __str__(self):
        return (f"Author - <{self.author}>; post_id - <{self.id}> "
                f"text part - <{self.text[:15]}>.")

    class Meta:
        ordering = ["-pub_date"]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-created"]


class Follow(models.Model):
    user = models.ForeignKey(User, related_name='followers',
                             on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followings',
                                  on_delete=models.CASCADE)

    def __str__(self):
        return f"Подписчик {self.user}, подписан на {self.following}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "following"],
                                    name="unique follow"),
            models.CheckConstraint(check=~models.Q(
                                   user=models.F("following")),
                                   name='following to yourself ')
        ]
        ordering = ["following__username"]
