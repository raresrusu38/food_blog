from django.urls                    import path
from .views                         import IndexView, PostDetail

app_name = "posts"

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('detail/<int:pk>/<slug:slug>/', PostDetail.as_view(), name='post-detail'),
]
