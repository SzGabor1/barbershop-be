from django.db import models
from django.conf import settings
from django.db.models import Q
User = settings.AUTH_USER_MODEL #auth.User 

class NewsQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs

class NewsManager(models.Manager):
    def get_queryset(self, *args,**kwargs):
        return NewsQuerySet(self.model, using=self._db)
    
    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)

class News(models.Model):
#    owner = models.ForeignKey('auth.User', related_name='news', on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1, null = True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=True)
    
    objects = NewsManager()
    
    def get_absolute_endpont(self):
        return f'/api/news/{self.pk}/'
    
    @property
    def endpoint(self):
        return self.get_absolute_endpont()
        
    