
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import News
from . import validators
from api.serializers import UserPublicSerializer


class NewsInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='news-detail',
            lookup_field='pk',
            read_only=True
    )
    title = serializers.CharField(read_only=True)

class NewsSerializer(serializers.ModelSerializer):
    
    #related_news = NewsInlineSerializer(source='user.news_set.all', many=True, read_only=True)
    owner = UserPublicSerializer(source = 'user', read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='news-detail', lookup_field='pk')

    #email = serializers.EmailField(write_only=True)
    
    #?validation
    title = serializers.CharField(validators=[validators.validate_title_no_curse,
                                              validators.unique_news_title])
  #  name = serializers.CharField(source='user.email', read_only=True)
    class Meta:
        model = News
        fields = [
            'owner',
            'url',
            'edit_url',
            'pk',
            'endpoint',
    #        'name',
            'title',
            'public',
       #     'related_news',
            'content',
            'created_at',
            'updated_at'
        ]
        
    # def validate_title(self, value):
    #     qs = News.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f'{value} Is already is a Title')
    #     if len(value) < 5:
    #         raise serializers.ValidationError('Title must be at least 5 characters long')
    #     return value
        
    # def create(self, validated_data):
    #     #email = validated_data.pop('email')
    #     return super().create(validated_data)
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     return super().update(instance, validated_data)


    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('news-edit', kwargs={'pk': obj.pk}, request=request)
