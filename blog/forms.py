from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Post

class AddCommentForm(forms.Form):
	post_choices = list()
	for post_obj in Post.objects.all():
		post_choices.append((post_obj.id, post_obj.title))
	post_id = forms.ChoiceField(
		choices=tuple(post_choices),
	)

	text = forms.CharField(
		max_length=500, 
		help_text="The text to display in the comment",
		widget=forms.Textarea
	)

	def clean_text(self):
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

	def clean_post_id(self):
		"""Validates the post id choice option."""
		data = self.cleaned_data['post_id']

		# Checks that a choice is selected
		if not data:
			raise ValidationError(_('Invalid Comment - no post selected'))

		return data


class AddPostForm(forms.Form):
	title = forms.CharField(
		max_length=60,
	)
	text = forms.CharField(
		help_text="The text to be displayed in the body of the blog post",
		widget=forms.Textarea,
	)

	def clean_title(self):
		"""Vaildates form data."""
		data = self.cleaned_data['title']

		# Check that there is a title
		if len(data) < 1:
			raise ValidationError(_('Invalid Post - no title entered'))
		# Check that the title is not too long
		if len(data) > 60:
			raise ValidationError(_('Invalid Post - title too long (max 60 characteres)'))

		return data

	def clean_text(self):
		"""Validates the text body of the potential blog post."""
		data = self.cleaned_data['text']


		# Check that there is text
		if len(data) < 1:
			raise ValidationError(_('Invalid Post - no body entered'))

		return data


"""
Very true; the entire oxidative phosphorylation process is mind-bending to think about!
Do any of you ever take a moment to step back and imagine the complexity that goes into the most elementary functions of your cell(s)? I do quite often. I'm regularly stunned by the many distinct protein micromachine megalopolises that reside throughout my cell membrane. They are towering (in the smallest sense possible), seemingly messy structures, which at first glance you'd guess were thrown together haphazardly. This is quite an understandable assumption to make, as the evolutionary forces which guided their shapes were not selecting for understandability or readability, but rather for pure function. A great foray into molecular machinery is the ATP Synthase protein. This synthase is secured into a membrane that has on each side of it, a differing concentration of hydrogen ions (protons). The protons on the side of the membrane with the higher relative concentration of ions, will desperately "want" to move to the size with the lower concentration, all in the pursuit of equilibrium. ATP Synthase ingeniously offers those protons a path to the destination they so desperately wish to get to, with a cost. The protons must turn an amino acid turbine in the synthase (much like water spinning a watermill as it rushes past), thereby transferring mechanical energy through an amino acid crankshaft in the center of the synthase, which delivers mechanical energy to another group of amino acids at the tip of the synthase that will use this energy to essentially create a little packet of now portable energy able to be used elsewhere in the cell: ATP. It should be noted that this is heavily simplified for the purpose of conciseness and not being overly esoteric. There is much more to be said about this synthase alone as well as the process mentioned, however, I believe that my original point has been made already (without even mentioning that this single protein is replicated hundreds of thousands of time in a single mitochondrion and a single cell may have thousands of mitochondria!), which is that I believe we should all bathe in the wonder of biology a bit more often. 
"""