from django import forms
from .models import user_tbl


class register_user(forms.ModelForm):

    class Meta:
        model = user_tbl
        fields = '__all__'
