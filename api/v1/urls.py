from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

router = DefaultRouter()
router.register('customers', views.CustomerViewSet, basename='customers')
router.register('quotes', views.QuoteViewSet, basename='quotes')
router.register('policies', views.PolicyViewSet, basename='policies')

urlpatterns = router.urls
