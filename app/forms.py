from django import forms
from .models import Category, Post


class PostSearchForm(forms.Form):
    key_word = forms.CharField(
        label='検索キーワード',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'autocomplete': 'off',
                                      'placeholder': 'Keyword',
                                      })
    )

    category = forms.ModelChoiceField(
        label='カテゴリ',
        required=False,
        queryset=Category.objects.order_by('name'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
