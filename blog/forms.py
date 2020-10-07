from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class AddCommentForm(forms.Form):
	text = forms.CharField(
		max_length=500, 
		help_text="The text to display in the comment",
		widget=forms.Textarea
	)

	def clean(self):
		"""
		Validates the text provided by the user to be added to the post.
		"""
		data = self.cleaned_data['text']

		# Check that there is text
		if len(data) < 1:
			raise ValidationError(_('Invalid Comment - no text entered'))

		# Checks that the max_length was not exceeded
		if len(data) > 500:
			raise ValidationError(_('Invalid Comment - maximum length exceeded'))

		return data