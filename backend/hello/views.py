from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class HelloApiView(APIView):

    def get(self,request, format=None):

        return Response({"Status":"Nuestra primera solicitud con DRFF !!!"}, status=status.HTTP_200_OK)
