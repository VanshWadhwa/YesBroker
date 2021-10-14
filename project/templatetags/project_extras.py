from django import template

register = template.Library()

@register.simple_tag
def my_url(value , field_name , urlencode = None):
    url = '?{}={}'.format(field_name , value)

    if urlencode:
        querysting = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0]!=field_name , querysting)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)

    return url 