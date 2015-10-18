from django.db import models
from django.db.models import F
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Project(models.Model):
    name = models.CharField(max_length=255,
                            null=False,
                            unique=True,
                            verbose_name='Name')

    slug = models.SlugField(max_length=50)

    base_language = models.ForeignKey('hicks_language.Language',
                                      related_name='project_base_language')

    supported_languages = models.ManyToManyField('hicks_language.Language')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Definition(models.Model):
    description = models.TextField(null=False,
                                   verbose_name='Description')

    project = models.ForeignKey(to='Project',
                                related_name='definitions')

    def __str__(self):
        return self.description

    def source_terms(self):
        return self.terms.filter(language=F('definition__project__base_language'))


@python_2_unicode_compatible
class Term(models.Model):
    term = models.TextField(null=False,
                            verbose_name='Term')

    definition = models.ForeignKey('Definition',
                                   related_name='terms')

    language = models.ForeignKey('hicks_language.Language',
                                 related_name='term_language')

    def __str__(self):
        return self.term
