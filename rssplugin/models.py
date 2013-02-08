from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class RSSPlugin(CMSPlugin):
    count = models.IntegerField(default=6)
    title = models.CharField(max_length=200,default="Community News",null=True,help_text=_("If you specified this value, it will replace feed's title"))
    rss_url = models.URLField()
    open_in_new_window = models.BooleanField()
    cache_time = models.IntegerField(verbose_name=_("Cache time in seconds"))
    def __unicode__(self):
	    return self.title
