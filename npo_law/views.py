from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

import npo_law
from npo_law.models import NPOLaw
from npo_law.serializers import NPOLawSerializer


class NPOLawAPIView(APIView, PageNumberPagination):
    allow_methods = ['GET', 'POST']
    serializer_class = NPOLawSerializer

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', '')
        npolaw = NPOLaw.objects.filter(Q(title__icontains=query) |
                                       Q(description__icontains=query))

        results = self.paginate_queryset(npolaw,
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
        npolaw = NPOLaw.objects.create(title=title,
                                       description=description,
                                       created_date=created_date,
                                       file=file)
        npolaw.save()
        return Response(data=self.serializer_class(npo_law).data,
                        status=status.HTTP_201_CREATED)


class NPOLawDetailAPIView(APIView):
    allow_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = NPOLawSerializer

    def get(self, request, id):
        law = NPOLaw.objects.get(id=id)
        return Response(data=self.serializer_class(law).data)

    def put(self, request, id):
        law = NPOLaw.objects.get(id=id)
        title = request.data.get('title')
        description = request.data.get('description')
        file = request.data.get('file')
        law.title = title
        law.description = description
        law.file = file
        law.save()
        return Response(data=self.serializer_class(law).data,
                        status=status.HTTP_202_ACCEPTED)

    def delete(self, request, id):
        law = NPOLaw.objects.get(id=id)
        law.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

