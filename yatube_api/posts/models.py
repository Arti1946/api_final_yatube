from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.TextField()
    slug = models.SlugField(unique=True)
    description = models.TextField

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    text = models.TextField(blank=False, null=False)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
        )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True
        )
    group = models. IntegerField(null=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
        )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
        )
    text = models.TextField(blank=False, null=False)
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
        )


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follow")
    following = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="following")

    def __str__(self):
        return f'{self.user} {self.following}'
