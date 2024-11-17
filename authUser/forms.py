from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from authUser.models import CustomUser


class StyleFormMixin:
    """
    Класс Mixin для стилизации форм.
    """

    def __init__(self, *args, **kwargs):
        """
        Инициализация класса StyleFormMixin.
        """
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """
    Класс для формы регистрации пользователя.
    """
    class Meta:
        model = CustomUser
        fields = (
            'role', 'avatar', 'phone', 'email', 'first_name', 'last_name', 'date_of_birth', 'password1', 'password2',
        )


class UserUpdateForm(StyleFormMixin, UserCreationForm):
    """
    Класс для формы редактирования пользователя.
    """
    class Meta:
        model = CustomUser
        fields = (
            'avatar', 'phone', 'email', 'first_name', 'last_name', 'date_of_birth',
        )


class DoctorForm(StyleFormMixin, UserChangeForm):
    """
    Класс для формы просмотра профиля врача.
    """
    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = CustomUser.objects.filter(role='doctor')

    class Meta:
        model = CustomUser
        fields = ('description', 'speciality', 'education', 'experience')


class DoctorProfileForm(StyleFormMixin, UserChangeForm):
    """
    Класс для формы своего профиля врача.
    """
    class Meta:
        model = CustomUser
        fields = (
            'description', 'speciality', 'education', 'experience'
        )
