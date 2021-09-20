from django.urls import path

from commentapp.views import CommentCreateView, CommentDeleteView
from projectapp.views import ProjectCreateView, ProjectDetailView, ProjectListView
from subscribeapp.views import SubscriptionView

app_name = "subscribeapp"

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
    # path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),
    # path('update/<int:pk>', CommentUpdateView.as_view(), name='update'),
    # path('create/', ProjectCreateView.as_view(), name='create'),
]
