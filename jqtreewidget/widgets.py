import json

from django.forms.widgets import Select
from django.forms.widgets import SelectMultiple
from django.template import Context
from django.template.loader import get_template
from django.utils.safestring import mark_safe


def get_jqtree_data(tree):
    """Return the tree as data for jqTree.
    """
    data = []

    for node in tree:
        if len(node) == 3 and node[2]:
            data.append({
                "id": node[0],
                "label": unicode(node[1]),
                "children": get_jqtree_data(node[2]),
            })
        else:
            data.append({
                "id": node[0],
                "label": unicode(node[1]),
            })

    return data


class JqTreeWidgetBase(object):
    """Base class for jqTree widgets.
    """

    def render(self, name, value, attrs=None):
        """Render the widget.
        """
        template = get_template(self.template)
        context = Context(self.get_context_data(name, value, attrs=attrs))
        return template.render(context)

    class Media(object):
        """Media.
        """

        css = {
            "all": ("jqtreewidget/css/jqtree.css", ),
        }

        js = ("jqtreewidget/js/jqtree.js", )


class JqTreeWidget(JqTreeWidgetBase, Select):
    """Single select jqTree widget.
    """

    template = "jqtreewidget/jqtreewidget.html"

    def __init__(self, attrs=None, choices=()):
        """Constructor.
        """
        super(JqTreeWidget, self).__init__(attrs=attrs, choices=choices)

        if attrs == None:
            attrs = {}
        self.tree = attrs.get("tree", ())

    def get_context_data(self, name, value, attrs=None):
        """Get the context data.
        """
        if value is None:
            value = ""

        data = {
            "name": name,
            "value": value,
            "data": mark_safe(json.dumps(get_jqtree_data(self.tree))),
        }
        return data


class JqTreeWidgetMultiple(JqTreeWidgetBase, SelectMultiple):
    """Multiple select jqTree widget.
    """

    template = "jqtreewidget/jqtreewidgetmultiple.html"

    def __init__(self, attrs=None, choices=()):
        """Constructor.
        """
        super(JqTreeWidgetMultiple, self).__init__(attrs=attrs, choices=choices)

        if attrs == None:
            attrs = {}
        self.tree = attrs.get("tree", ())

    def get_context_data(self, name, value, attrs=None):
        """Get the context data.
        """
        if value is None:
            value = []

        data = {
            "name": name,
            "value": mark_safe(json.dumps(value)),
            "data": mark_safe(json.dumps(get_jqtree_data(self.tree))),
        }
        return data
