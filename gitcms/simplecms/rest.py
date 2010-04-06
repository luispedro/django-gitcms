
# Copyright 2009-2010 Luis Pedro Coelho <luis@luispedro.org>
# Part of django-gitcms
# LICENSE: Affero GPL v3

from docutils.core import publish_parts

from django.conf import settings
from django.utils.encoding import smart_str, force_unicode
from django.utils.safestring import mark_safe

from . import sourcecode_directive

_precontent = '''\
**********
Fake Title
**********
+++++++++++++
Fake Subtitle
+++++++++++++

'''


def preprocess_rst_content(value):
    # This is adapted from django source
    value = _precontent + value
    docutils_settings = getattr(settings, "RESTRUCTUREDTEXT_FILTER_SETTINGS", {})
    parts = publish_parts(source=smart_str(value), writer_name="html4css1", settings_overrides=docutils_settings)
    return mark_safe(force_unicode(parts["fragment"]))

