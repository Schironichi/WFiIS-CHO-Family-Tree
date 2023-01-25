from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
        'name',
        'surname',
        'birth',
        'death'
        ]

class RelationForm(forms.Form):
        
    person_from = forms.ChoiceField(choices=[])
    relation = forms.ChoiceField(choices=[
        ('MARRIED', 'is married to'),
        ('PARENT', 'is a parent of'),
        ('CHILD', 'is a child of'),
    ])
    person_to = forms.ChoiceField(choices=[])
    
    def __init__(self, *args, **kwargs):
        super(RelationForm, self).__init__(*args, **kwargs)
        nodes = list(map(lambda x: (x.uid, x.name + ' ' + x.surname), Person.nodes.all()))
        
        self.fields['person_from'].choices = nodes
        self.fields['person_to'].choices = nodes
