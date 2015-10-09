from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the ProjectListView
    url(
        regex=r'^$',
        view=views.ProjectListView.as_view(),
        name='list'
    ),
]
