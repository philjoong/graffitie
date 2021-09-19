from django.urls import path

from commentapp.views import CommentCreateView, CommentDeleteView
from projectapp.views import ProjectCreateView, ProjectDetailView, ProjectListView

app_name = "projectapp"

urlpatterns = [
    path('list/', ProjectListView.as_view(), name='list'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),
    # path('update/<int:pk>', CommentUpdateView.as_view(), name='update'),
    path('create/', ProjectCreateView.as_view(), name='create'),
]
