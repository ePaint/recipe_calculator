from django.utils.deprecation import MiddlewareMixin


class HTMXMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.base_template = (
            "layout/fragment.html" if request.htmx else "layout/base.html"
        )
