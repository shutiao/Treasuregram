from django import forms
from .models import Treasure

# By inheriting from forms.ModelForm instead pf forms.Form
# We'll be able to automatically work with form fields in the view and template
# 
class TreasureForm(forms.ModelForm):
    # The Meta class allows us to define properties that help us link the form and model together
    # The name pf this class will always to "Meta"
    class Meta:
        # The model property is used to define which model the form will be created from
        # which is our case is the Treasure model.
        model = Treasure
        # the fields property defines which model fields should have coresponding form inputs.
        # the HTML form will display labels and iputs for these five fields
        fields = ['name', 'value', 'location', 'material', 'img_url']
       