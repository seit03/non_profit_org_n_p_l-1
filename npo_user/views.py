from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from npo_user.models import NPOUser
from npo_user.serializers import NPOUserSerializer


class NPOUserAPIView(APIView, PageNumberPagination):
    allow_methods = ['GET', 'POST']
    serializer_class = NPOUserSerializer

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', '')
        npolaw = NPOUser.objects.filter(Q(title__icontains=query) |
                                       Q(description__icontains=query))

        results = self.paginate_queryset(npolaw,
                                         request,
                                         view=self)
        return self.get_paginated_response(self.serializer_class(results,
                                                                 many=True,
                                                                 context={'request': request}).data)

    def post(self, request, *args, **kwargs):
        user_type = request.data.get('user_type')
        user_name = request.data.get('user_name')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        data_joined = request.data.get('data_joined')
        is_active = request.data.get('is_active')
        is_staff = request.data.get('is_staff')
        objects = request.data.get('objects')

        npouser = NPOUser.objects.create(user_type=user_type,
                                         user_name=user_name,
                                         email=email,
                                         first_name=first_name,
                                         last_name=last_name,
                                         data_joined=data_joined,
                                         is_active=is_active,
                                         is_staff=is_staff,
                                         objects=objects)
        npouser.save()
        return Response(data=self.serializer_class(npouser).data,
                        status=status.HTTP_201_CREATED)


class NPOUserDetailAPIView(APIView):
    allow_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = NPOUserSerializer

    def get(self, request, id):
        npouser = NPOUser.objects.get(id=id)
        return Response(data=self.serializer_class(npouser).data)

    def put(self, request, id):
        npouser = NPOUser.objects.get(id=id)
        text = request.data.get('text')
        created_date = request.data.get('created_date')
        updated_date = request.data.get('updated_date')
        npouser.text = text
        npouser.created_date = created_date
        npouser.updated_date = updated_date
        npouser.save()
        return Response(data=self.serializer_class(npouser).data,
                        status=status.HTTP_202_ACCEPTED)

    def delete(self, request, id):
        npouser = NPOUser.objects.get(id=id)
        npouser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)