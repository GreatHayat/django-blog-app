from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile, Comment

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)
    #email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={'placeholder': "Email"}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class ProfileEditForm(forms.ModelForm):
    status = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 3, 'placeholder': 'What is on your mind?'}
        ),
        max_length=100,
        help_text='The max length of the text is 100.'
        )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Write something about yourself'}
        ),
        max_length=500,
        help_text='The max length of the text is 500.'
        )
    class Meta:
        model = Profile
        fields = ['title', 'status', 'description', 'profile_image']

class AddNewPostForm(forms.ModelForm):
    #created_by = forms.CharField(max_length=30)
    class Meta:
        model = Post
        fields = ['title', 'category', 'post_content', 'feature_image']

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'post_content', 'feature_image']


class CommentForm(forms.ModelForm):
    comment_msg = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 3, 'placeholder': 'Write something about yourself'}
        ),
        max_length=500
        )
    class Meta:
        model = Comment
        fields = ['comment_msg']
