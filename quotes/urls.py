from django.contrib import admin
from django.urls import path, include
from rest_framework import serializers, routers, viewsets
from rest_framework.response import Response

from quote import views
from quote.models import Quote, Author


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['quote', 'author', 'id']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'id']


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def list(self, request, *args, **kwargs):
        queryset = Quote.objects.getRandomQuote()
        authors = Author.objects.getFourRandomAuthors()
        data = {
            'quote': QuoteSerializer(queryset).data,
            'authors': AuthorSerializer(authors, many=True).data
        }
        return Response(data)


router = routers.DefaultRouter()
router.register(r'quotes', QuoteViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
