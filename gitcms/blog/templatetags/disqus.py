from django import template
import settings

register = template.Library()

if hasattr(settings,'DISQUS_SHORTNAME'):
    @register.inclusion_tag('blog/disqus.html')
    def disqus_thread(post):
        return {
            'disqus_shortname' : settings.DISQUS_SHORTNAME,
            'unique_identifier' : post.slug,
        }
else:
    @register.simple_tag
    def disqus_thread(_):
        return ''
            
    
