from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#this for get an absolute url
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,  # This is a field intended to be used in URLs
        unique_for_date='publish') # This ensures that there will be only one post with a slug for agiven date, and thus, you can retrieve single posts using the date and slug
    author = models.ForeignKey(User,   #: This field defines a many-to-one relationship, user can write any number of posts
        on_delete=models.CASCADE, # Using CASCADE, you specify that when the referenced user is deleted, the database will also delete all related blogposts.
        related_name='blog_posts') # "related_name" will allow you to access related objects easily.
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now) #: This datetime indicates when the post was published
    created = models.DateTimeField(auto_now_add=True) # auto_now_add, the date will be saved automatically when creating an object.
    updated = models.DateTimeField(auto_now=True) #auto_now here, the date will be updated automatically whensaving an object.
    status = models.CharField(max_length=10, # You use a choices parameter,so the value of this field can only be set to one of the given choices.
        choices=STATUS_CHOICES,
        default='draft')

    def get_absolute_url(self):  # to link to specific posts.
        return reverse('blog:post_detail',
        args=[self.publish.year,
        self.publish.month,
        self.publish.day, self.slug])

    # With Meta class  You tell Django to sort results by the publish field in descending order by default when you query the database.
    #You specify the descending order using the negative prefix. By doing this, posts
    #published recently will appear first.
    class Meta:
            ordering = ('-publish',)

    def __str__(self):   #__str__  is the default human-readable representation of the object
        return self.title
