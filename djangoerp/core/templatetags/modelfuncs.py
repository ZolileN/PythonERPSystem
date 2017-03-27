#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This file is part of the django ERP project.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

__author__ = 'Zolile Nonzapa <zolile@mlkcomputer.co.za>'
__copyright__ = 'Copyright (c) 2017 Zolile Nonzapa'
__version__ = '0.0.1'

from django import template
from django.db import models
from django.utils.translation import ugettext_lazy as _

register = template.Library()

@register.filter
def model_name(obj):
    """Returns the model name for the given instance.

    Example usage: {{ object|model_name }}
    """
    if isinstance(obj, models.Model):
        return obj._meta.verbose_name or _(obj.__class__.__name__)
    return ''
