from rest_framework import status, serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


class ViewSetSerializerMixin:
    create_serializer_class: serializers.Serializer | None = None
    update_serializer_class: serializers.Serializer | None = None
    list_serializer_class: serializers.Serializer | None = None

    def _get_serializer_class(
        self,
        *args,
        **kwargs,
    ):
        if self.action == "create":  # type: ignore
            return self.create_serializer_class
        if self.action in {"update", "partial_update"}:  # type: ignore
            return self.update_serializer_class or self.create_serializer_class
        if self.action == "list":  # type: ignore
            return self.list_serializer_class
        return None

    def get_serializer_class(self):
        serializer_class = self._get_serializer_class()
        if serializer_class:
            return serializer_class
        return super().get_serializer_class()  # type: ignore


class ViewSetCreateMixin:
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ViewSetGetMixin:
    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        elif self.request.user.is_authenticated:
            return super().get_queryset().filter(creator=self.request.user)



class CustomModelViewSet(ViewSetSerializerMixin, ViewSetCreateMixin, ViewSetGetMixin, ModelViewSet):
    pass
