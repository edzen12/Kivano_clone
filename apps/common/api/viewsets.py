from rest_framework.viewsets import ReadOnlyModelViewSet


class BasedReadOnlyModelViewSet(ReadOnlyModelViewSet):
    serializer_classes = {}

    def get_serializer_class(self):
        return self.serializer_classes.get(
            self.action,
            super().get_serializer_class(),
        )