from django.db import models


def upload_to(instance, filename):
    return '%s' % filename


class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новость'
    title = models.CharField(max_length=100)

    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to='upload_to')
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class NewsFavorite(models.Model):
    news = models.ForeignKey(News,
                             on_delete=models.CASCADE,
                             related_name='news_newsfavorite')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
