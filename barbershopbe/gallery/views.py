from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import BlobModel
from .serializers import BlobModelSerializer
import base64
from api.mixins import StaffEditorPermissionMixin
from rest_framework.generics import DestroyAPIView

class ImageUploadView(APIView,
                      StaffEditorPermissionMixin):
    def post(self, request, *args, **kwargs):
        image_data = request.data.get('blob_data')
        if not image_data:
            return Response({"error": "No image data provided"}, status=status.HTTP_400_BAD_REQUEST)

        blob_data = image_data.read()
        encoded_blob_data = base64.b64encode(blob_data)
        encoded_blob_data_str = encoded_blob_data.decode('utf-8')

        data = {
            'type': request.data.get('type'),
            'blob_data': encoded_blob_data_str
        }
        serializer = BlobModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlobListView(ListAPIView):
    queryset = BlobModel.objects.all()
    serializer_class = BlobModelSerializer


class BlobDeleteView(DestroyAPIView,
                     StaffEditorPermissionMixin):
    queryset = BlobModel.objects.all()
    serializer_class = BlobModelSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Blob deleted successfully"}, status=status.HTTP_204_NO_CONTENT)