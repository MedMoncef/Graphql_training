from django.http import HttpResponse
from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 2
    page_query_param = 'p'


def get_paginated_response(self, data):
    return Response({
        'next': self.get_next_link(),
        'previous': self.get_previous_link(),
        'count': self.page.paginator.count,
        'total_pages': self.page.paginator.num_pages,
        'page_number': self.page.number,
        'per_page': self.page.paginator.per_page,
        'results': data
    })
