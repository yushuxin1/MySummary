from django import forms

class ProductForm(forms.Form):
    url = forms.URLField(max_length=300, label='图片地址链接')
    file = forms.FileField()
    # photo = forms.ImageField(label='头像')