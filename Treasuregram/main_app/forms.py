from django import forms

# Our form class look almost identical to model's
# In a similar way that a model class’s fields map to database fields, 
# a form class’s fields map to HTML form <input> elements. 
#
class TreasureForm(forms.Form):
    name = forms.CharField(label='Name', max_length = 100)
    value = forms.DecimalField(label='Value', max_digits = 10, decimal_places = 2)
    material = forms.CharField(label='Location', max_length = 100)
    location = forms.CharField(label='Location', max_length = 100)
    img_url = forms.CharField(label='Image URL', max_length = 100)