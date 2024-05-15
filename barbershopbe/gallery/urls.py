from django.urls import path
from .views import ImageUploadView, BlobListView, BlobDeleteView

urlpatterns = [
    path('upload/', ImageUploadView.as_view(), name='image_upload'),
    path('blobs/', BlobListView.as_view(), name='blob_list'),
    path('blobs/<int:pk>/', BlobDeleteView.as_view(), name='blob_delete'),
]
