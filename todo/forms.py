from django import forms
from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    deadline = forms.DateTimeField(
        widget=forms.DateInput(attrs={"type": "datetime-local", "class": "form-control"}),
        required=False
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "done", "tags"]
        widgets = {
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "done": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
