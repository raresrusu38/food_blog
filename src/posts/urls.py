from django.urls                    import path
from .views                         import CategoryDetail, IndexView, PostDetail

app_name = "posts"

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('detail/<int:pk>/<slug:slug>/', PostDetail.as_view(), name='post-detail'),
    path('category/<int:pk>/<slug:slug>/', CategoryDetail.as_view(), name='category-detail'),
]
