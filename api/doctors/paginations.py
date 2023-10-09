from rest_framework.pagination import PageNumberPagination


class DoctorPagination(PageNumberPagination):
    page_size = 10
    page_query_param = "page"
    page_size_query_param = (
        "page_size"
    )
    max_page_size = 20


class ServicePagination(PageNumberPagination):
    page_size = 300
    page_query_param = "page"
    page_size_query_param = "page_size"
    max_page_size = 300
