from rest_framework import serializers
from .models import BlobModel
import base64

class BlobModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlobModel
        fields = ['pk', 'type', 'blob_data']

    def to_internal_value(self, data):
        blob_data_str = data.get('blob_data')
        data = super().to_internal_value(data)
        if blob_data_str:
            try:
                blob_data_bytes = base64.b64decode(blob_data_str)
                data['blob_data'] = blob_data_bytes
            except ValueError:
                raise serializers.ValidationError("Invalid base64 data for blob_data")
        return data
