from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from npo_news.models import News
from npo_news.serializers import NewsSerializer


class NewsAPIView(APIView, PageNumberPagination):
    allow_methods = ['GET', 'POST']
    serializer_class = NewsSerializer

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', '')
        news = News.objects.filter(Q(title__icontains=query) |
                                   Q(description_icontains=query))

        results = self.paginate_queryset(news,
                                         request,
                                         view=self)
        return self.get_paginated_response(self.serializer_class(results,
                                                                 many=True,
                                                                 comtext={'request': request}).data)

    def post(self, request, *args, **kwargs):
        title = request.data.get('title')
        description = request.data.get('description')
        link = request.data.get('link')
        image = request.data.get('image')
        news = News.objects.create(title=title,
                                   description=description,
                                   link=link,
                                   image=image)

        news.save()
        return Response(data=self.serializer_class(news).data,
                        status=status.HTTP_201_CREATED)


class NewsDetailAPIView(APIView, PageNumberPagination):
    allow_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = NewsSerializer

    def get(self, request, id):
        news = News.objects.get(id=id)
        return Response(data=self.serializer_class(news).data)

    def put(self, request, id):
        news = News.objects.get(id=id)
        title = request.data.get('title')
        description = request.data.get('description')
        link = request.data.get('link')
        image = request.data.get('image')
        news.title = title
        news.description = description
        news.link = link
        news.image = image
        news.save()

        return Response(data=self.serializer_class(news).data,
                        status=status.HTTP_202_ACCEPTED)

    @staticmethod
    def delete(request, id):
        news = News.objects.get(id=id)
        news.delete()
        return Response(status=status.HTTP_204_OK)