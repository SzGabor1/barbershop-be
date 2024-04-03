from rest_framework import serializers


class UserNewsInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name='news-detail', lookup_field='pk', read_only=True)
    title = serializers.CharField(read_only=True)

class UserPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    
    # other_news = serializers.SerializerMethodField(read_only=True)
    
    # def get_other_news(self, obj):
    #     user = obj
    #     my_news_qs = user.news_set.all()[:5]
    #     return UserNewsInlineSerializer(my_news_qs, many=True, context = self.context).data