from django.db import models
from django.utils.translation import ugettext_lazy as _

class Feedback(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    content = models.TextField()

    class Meta:
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedbacks')

    def __unicode__(self):
        return "%s - %s" % (self.username, self.content)
    
