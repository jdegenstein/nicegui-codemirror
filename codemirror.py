from typing import Callable, Optional

from nicegui.element import Element
from nicegui.elements.mixins.value_element import ValueElement
from nicegui.elements.mixins.disableable_element import DisableableElement


class CodeMirror(ValueElement, DisableableElement, component="codemirror.js"):
    VALUE_PROP = "value"
    LOOPBACK = False

    def __init__(
        self,
        value: str = "",
        on_change: Optional[Callable] = None,
        mode: str = "python",
    ) -> None:
        super().__init__(value=value, on_value_change=on_change)
        self._props["mode"] = mode

        def change_handler(e):
            self.value = e.args["value"]

        self.on("change", change_handler)

    def update(self) -> None:
        super().update()
        self.run_method("update")
