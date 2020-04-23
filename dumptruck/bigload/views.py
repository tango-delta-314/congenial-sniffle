from bigload.models import Trash
from bigload.serializers import TrashSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from bigload.tasks import create_trash


class TrashList(APIView):
    """
    List all trash.
    """
    def get(self, request, format=None):
        all_trash = Trash.objects.all()
        serializer = TrashSerializer(all_trash, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        creation_task = create_trash.apply_async(args=[
            'Test Create',
            'Test Test Create Content'
        ])

        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, format=None):

        all_trash = Trash.objects.all()
        for t in all_trash:
            t.delete()

        return Response({"status": "ok"})
