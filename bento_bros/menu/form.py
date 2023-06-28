from django import forms
from .models import Appetizer, MainCourse, Dessert


class AppForm(forms.ModelForm):
    class Meta:
        model = Appetizer
        fields = ["name", "price", "description"]


class MainForm(forms.ModelForm):
    class Meta:
        model = MainCourse
        fields = ["name", "price", "description"]


class DessertForm(forms.ModelForm):
    class Meta:
        model = Dessert
        fields = ["name", "price", "description"]
