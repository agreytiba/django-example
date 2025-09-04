from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from django.shortcuts import render

class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("Request URL:", request.path)
        if request.path.startswith('/blocked/'):
            return render(request, 'warning.html')
        
    def process_response(self, request, response):
        # Code to be executed for each request/response after
        # the view is called.
        print("Response Status Code:", response.status_code)
        response['X-App-Name'] = 'MyDjangoApp'
        response['X-Delevoper'] = 'agrey'
        response['X-Version'] = '2.0.0'
        return response

        