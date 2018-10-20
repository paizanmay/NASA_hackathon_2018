from rest_framework import routers

from api.views import ItemViewSet


router = routers.SimpleRouter()
router.register(r'item', ItemViewSet)
urlpatterns = router.urls
