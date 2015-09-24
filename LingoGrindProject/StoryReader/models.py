from django.db import models

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self


class Story(models.Model):
    title = models.CharField(max_length = 200)
    englishStory = models.TextField(default = 'Story Here')
    chineseStory = models.TextField(default = 'Aqui se queda el cuento')
    spanishStory = models.TextField(default =  'gushi zheli')
    body = models.TextField()
    slug = models.SlugField()
    pub = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Story Entry"
        verbose_name_plural = "Story Entries"
        ordering = ["-created"]