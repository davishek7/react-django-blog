from rest_framework.routers import DefaultRouter
from .views import PostList

app_name = 'api'

router = DefaultRouter()
router.register('', PostList,basename='post')
urlpatterns = router.urls


# urlpatterns = [
# 	path('',PostList.as_view(),name='listcreate'),
# 	path('<int:pk>/',PostDetail.as_view(),name='detailcreate'),
# ]