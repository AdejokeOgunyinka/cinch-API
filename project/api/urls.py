from rest_framework.routers import SimpleRouter

from .views import (
    OtpsViewSet,
    AuthsViewSet,
    ArtistsViewSet,
    PasswordsViewSet,
)


router = SimpleRouter(trailing_slash=False)

# Authentication Routes
router.register(r'auth', AuthsViewSet, basename='auth')
router.register(r'otps', OtpsViewSet, basename='otps')
router.register(r'passwords', PasswordsViewSet, basename='passwords')

# # Artists Routes
router.register(r'artists', ArtistsViewSet, basename='artists')

urlpatterns = router.urls

