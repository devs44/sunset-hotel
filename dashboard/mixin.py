class QuerysetMixin(object):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class DeleteMixin(object):
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
