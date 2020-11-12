from rest_framework.routers import SimpleRouter
from .views import (
    OtpsViewSet,
    AuthsViewSet,
    ArtistsViewSet,
    PasswordsViewSet,
    LocationViewset,
    BankListViewSet,
    AccountVerifyViewSet,
)

router = SimpleRouter(trailing_slash=False)
# Authentication Routes
router.register(r'auth', AuthsViewSet, basename='auth')
router.register(r'otps', OtpsViewSet, basename='otps')
router.register(r'passwords', PasswordsViewSet, basename='passwords')
router.register(r'locations', LocationViewset, basename='locations')

# Payment Routes
router.register(r'banks', BankListViewSet, basename='banks')
router.register(r'add_account', AccountVerifyViewSet, basename='add_account')

# # Artists Routes
router.register(r'artists', ArtistsViewSet, basename='artists')
urlpatterns = router.urls
