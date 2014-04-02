``jqtreewidget``
================

Tree widgets for Django, based on jqTree.


REQUIREMENTS
------------

- Django (>= 1.6)
- jQuery (>= 1.8.3)


USAGE
-----

1. Add ``jqtreewidget`` to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        "jqtreewidget",
    )

2. In your code, define the choices and the tree::

    MY_CHOICES = (
        ("", "--"),
        ("foo", "Foo"),
        ("bar", "Bar"),
        ("baz", "Baz"),
        ("qux", "Qux"),
        ("vim", "Vim"),
        ("dav", "Dav"),
    )
    MY_TREE = (
        ("foo", "Foo", (
            ("bar", "Bar"),
            ("baz", "Baz"),
        )),
        ("qux", "Qux", (
            ("vim", "Vim"),
            ("dav", "Dav"),
        )),
    )

3. In your code, define the fields and widgets::

    from jqtreewidget.widgets import JqTreeWidget
    from jqtreewidget.widgets import JqTreeWidgetMultiple

    ...

    class MyForm(Form):

        my_single_select = ChoiceField(
            label=u"My Single Select",
            required=False,
            initial="",
            choices=MY_CHOICES,
            widget=JqTreeWidget(attrs={"tree": MY_TREE}))

        my_multi_select = MultipleChoiceField(
            label=u"My Multi Select",
            required=False,
            initial=(),
            choices=MY_CHOICES[1:],
            widget=JqTreeWidgetMultiple(attrs={"tree": MY_TREE}))


CONTRIBUTORS
------------

- Bert Vanderbauwhede <bert.vanderbauwhede@ugent.be>


REMARKS
-------

The widgets in this package use jqTree (http://mbraak.github.io/jqTree/), a
tree widget for jQuery.  The following files from jqTree are included in this
package:

- ``jqtreewidget/static/jqtreewidget/css/jqtree.css``
- ``jqtreewidget/static/jqtreewidget/js/jqtree.js``

These files are released under the Apache license (see ``docs/APACHE.txt``).
