from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 10  # количество элементов на странице по умолчанию
    page_size_query_param = 'page_size'  # параметр, чтобы клиент мог изменить page_size
    max_page_size = 50  # максимальное количество элементов на странице
    page_query_param = 'page'  # параметр для номера страницы