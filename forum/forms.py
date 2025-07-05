from django import forms

from .models import Message, Tag, Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            "content",
        ]

class MessageForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
    )

    class Meta:
        model = Message
        fields = [
            "content",
        ]