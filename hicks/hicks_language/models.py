from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Language(models.Model):
    code = models.CharField(max_length=50,
                            null=False,
                            unique=True,
                            verbose_name='Code',
                            help_text='http://www.w3.org/International/articles/language-tags')
    display_name = models.CharField(max_length=255,
                                    null=False,
                                    verbose_name='Display Name')

    class Meta:
        ordering = ['code']

    def __str__(self):
        return u"{0} - {1}".format(self.display_name, self.code)
