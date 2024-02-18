from django.forms import ModelForm
from .models import *

class ClassroomForm(ModelForm):
    class Meta:
        model = Classroom
        fields = "__all__"

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"
        
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = "__all__"