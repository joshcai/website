from django import template

register = template.Library()

def tagcheck2(value, arg):
	"""Gets the value of the tag in request session"""

	return str(value.id)==str(arg)

register.filter('tagcheck2', tagcheck2)

def tag2(value, arg):
	if arg in value.tags.all():
		return True
	return False

register.filter('tag2', tag2)