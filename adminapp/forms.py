from django.contrib.auth import get_user_model

from authapp.forms import ShopUserEditForm


class AdminShopUserUpdateForm(ShopUserEditForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'password',
                  'email', 'age', 'avatar',
                  'is_staff', 'is_superuser', 'is_active')
