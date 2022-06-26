from cats.models import Breed
from django.forms import ModelForm


class BreedForm(ModelForm):
    class Meta:
        model = Breed
        fields = "__all__"
