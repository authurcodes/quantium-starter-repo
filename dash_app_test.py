from app import app
from dash import html


def flatten(component):
    items = [component]
    if hasattr(component, "children"):
        children = component.children
        if isinstance(children, (list, tuple)):
            for c in children:
                items.extend(flatten(c))
        elif children:
            items.extend(flatten(children))
    return items


def test_header_present():
    components = flatten(app.layout)

    # Correct way: check for html.H1 component and its text
    assert any(
        isinstance(c, html.H1) and
        c.children == "Soul Foods - Pink Morsel Sales Dashboard"
        for c in components
    )


def test_visualisation_present():
    components = flatten(app.layout)

    assert any(
        getattr(c, "id", None) == "sales-line-chart"
        for c in components
    )


def test_region_picker_present():
    components = flatten(app.layout)

    assert any(
        getattr(c, "id", None) == "region-radio"
        for c in components
    )

    




