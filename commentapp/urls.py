from django.urls import path

from commentapp.views import CommentCreateView, CommentDeleteView

app_name = "commentapp"

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),
    # path('detail/<int:pk>', CommentDetailView.as_view(), name='detail'),
    # path('update/<int:pk>', CommentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', CommentDeleteView.as_view(), name='delete'),
]
