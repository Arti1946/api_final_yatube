from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.serializers import ValidationError

from django.shortcuts import get_object_or_404

from api.permissions import UserActionsPermisiion
from api.v1.serializers import (
    CommentSerializer, GroupSerializer, PostSerializer, FollowSerializer
)
from posts.models import Group, Post, User


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related("author")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, UserActionsPermisiion]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

    def perform_update(self, serializer):
        user = self.request.user
        serializer.save(author=user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, UserActionsPermisiion]

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        new_queryset = post.comments.select_related("author")
        return new_queryset

    def perform_create(self, serializer):
        user = self.request.user
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        serializer.save(
            author=user,
            post=post,
        )

    def perform_update(self, serializer):
        user = self.request.user
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        serializer.save(
            author=user,
            post=post,
        )


class CreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass


class FollowViewSet(CreateListViewSet):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        user = self.request.user
        follow = get_object_or_404(User, username=user)
        new_queryset = follow.follow.select_related("following")
        return new_queryset

    def perform_create(self, serializer):
        user = self.request.user
        if serializer.validated_data["following"] == user:
            raise ValidationError("Нельзя подписаться на себя!")

        serializer.save(user=user)
