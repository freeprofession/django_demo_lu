from rest_framework.generics import ListAPIView
from rest_framework.response import Response


class ListApiView(ListAPIView):

    def get(self, request, *args, **kwargs):
        fields = []
        if hasattr(self, 'fields'):
            fields = self.fields

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, fields=fields)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True, fields=fields)
        return Response(serializer.data)
