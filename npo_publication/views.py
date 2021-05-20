from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from npo_publication.models import Publication
from npo_publication.serializers import PublicationSerializer


class PublicationAPIView(APIView, PageNumberPagination):
    allow_methods = ['GET', 'POST']
    serializer_class = PublicationSerializer

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', '')
        publication = Publication.objects.filter(Q(title__icontains=query) |
                                                 Q(description__icontains=query))

        results = self.paginate_queryset(publication,
                                         request,
                                         view=self)
        return self.get_paginated_response(self.serializer_class(results,
                                                                 many=True,
                                                                 context={'request': request}).data)

    def post(self, request, *args, **kwargs):
        title = request.data.get('title')
        description = request.data.get('description')
        created_date = request.data.get('created_date')
        file = request.data.get('file')
        publication = Publication.objects.create(title=title,
                                                 description=description,
                                                 created_date=created_date,
                                                 file=file)
        publication.save()
        return Response(data=self.serializer_class(publication).data,
                        status=status.HTTP_201_CREATED)


class PublicationDetailAPIView(APIView):
    allow_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = PublicationSerializer

    def get(self, request, id):
        publication = Publication.objects.get(id=id)
        return Response(data=self.serializer_class(publication).data)

    def put(self, request, id):
        publication = Publication.objects.get(id=id)
        title = request.data.get('title')
        description = request.data.get('description')
        file = request.data.get('file')
        publication.title = title
        publication.description = description
        publication.file = file
        publication.save()
        return Response(data=self.serializer_class(publication).data,
                        status=status.HTTP_202_ACCEPTED)

    def delete(self, request, id):
        publication = Publication.objects.get(id=id)
        publication.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PublicationFavoriteAPIView(APIView):
    allow_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = PublicationSerializer

    def get(self, request, id):
        publication = Publication.objects.get(id=id)
        return Response(data=self.serializer_class(publication).data)

    def put(self, request, id):
        publication = Publication.objects.get(id=id)
        text = request.data.get('text')
        created_date = request.data.get('created_date')
        publication.text = text
        publication.created_date = created_date
        publication.save()
        return Response(data=self.serializer_class(publication).data,
                        status=status.HTTP_202_ACCEPTED)

    def delete(self, request, id):
        publication = Publication.objects.get(id=id)
        publication.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)