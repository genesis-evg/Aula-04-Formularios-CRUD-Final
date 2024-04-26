from django import forms

from .models import ranking


class rankingForm(forms.ModelForm):
  class Meta:
    model = ranking
    fields = "__all__"