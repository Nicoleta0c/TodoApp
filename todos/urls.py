from rest_framework.routers import DefaultRouter

from todos import views

router = DefaultRouter()
router.register('tasks', views.TaskViewSet)

urlpatterns = router.urls
