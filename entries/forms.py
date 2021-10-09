from django.forms import ModelForm
from .models import Entries

class EntryForm(ModelForm):
    class Meta:
        model = Entries
        fields = ('title','text') 

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].widget.attrs.update({'class':'textarea','placeholder':"What's your title??"})
        self.fields['text'].widget.attrs.update({'class':'textarea','placeholder':"What's on your Mind??"})