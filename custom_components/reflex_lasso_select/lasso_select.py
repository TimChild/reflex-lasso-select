"""Reflex custom component LassoSelect."""

# For wrapping react guide, visit https://reflex.dev/docs/wrapping-react/overview/

from typing import List, Dict
import reflex as rx
from reflex.event import passthrough_event_spec

# Some libraries you want to wrap may require dynamic imports.
# This is because they they may not be compatible with Server-Side Rendering (SSR).
# To handle this in Reflex, all you need to do is subclass `NoSSRComponent` instead.
# For example:
# from reflex.components.component import NoSSRComponent
# class LassoSelect(NoSSRComponent):
#     pass


class LassoSelect(rx.Component):
    """LassoSelect component."""

    # The React library to wrap.
    library = "react-lasso-select"
    tag = "ReactLassoSelect"

    # If the tag is the default export from the module, you must set is_default = True.
    # This is normally used when components don't have curly braces around them when importing.
    # is_default = True

    # If you are wrapping another components with the same tag as a component in your project
    # you can use aliases to differentiate between them and avoid naming conflicts.
    # alias = "OtherLassoSelect"

    src: rx.Var[str]
    value: rx.Var[List[Dict[str, float]]]
    disabled: rx.Var[bool]

    on_change: rx.EventHandler[passthrough_event_spec(List[Dict[str, float]])]
    on_complete: rx.EventHandler[passthrough_event_spec(List[Dict[str, float]])]

    # To add custom code to your component
    # def _get_custom_code(self) -> str:
    #     return "const customCode = 'customCode';"


lasso_select = LassoSelect.create
