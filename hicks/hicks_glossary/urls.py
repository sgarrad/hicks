from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the ProjectListView
    url(  # /
          regex=r'^$',
          view=views.ProjectListView.as_view(),
          name='list'
          ),

    # URL pattern for the ProjectDetailView
    url(  # /test_project/
          regex=r'^(?P<slug>[^/]*)/$',
          view=views.ProjectDetailView.as_view(),
          name='detail'
          ),

    # URL pattern for the project language
    url(  # /test_project/fr-fr/
          regex=r'^(?P<project_slug>[^/]*)/(?P<language_code>[^/]*)/$',
          view=views.ProjectLanguageView.as_view(),
          name='language_detail'
          ),

    # URL pattern for the project language
    url(  # /test_project/fr-fr/terms
          regex=r'^(?P<project_slug>[^/]*)/(?P<language_code>[^/]*)/terms/?$',
          view=views.ProjectLanguageTermList.as_view(),
          name='project_language_term_list'
          ),
]
