from django import template


register = template.Library()

@register.simple_tag
def url_replace (request, field, value):
    """request url changes into the following formats when field='page', value=1:
    url = '/home/' => '/home/?page=1'
    url = '/?q=searchstring' => '/?q=searchstring&page=1'
    and so on.
    """
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()