from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# view for /api/book
class bookview(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'hi': 'django'})
        #return render(request, 'book.html')

book_view = bookview.as_view()