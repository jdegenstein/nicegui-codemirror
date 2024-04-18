from nicegui import ui

from codemirror import CodeMirror
from io import StringIO
from contextlib import redirect_stdout

from dataclasses import dataclass


@dataclass
class ReturnVal:
    value: str


rv = ReturnVal
rv.value = ""


def cbackhand(code, label):
    f = StringIO()
    with redirect_stdout(f):
        exec(code)
    rv.value = f.getvalue()
    label.set_text("asdf: " + rv.value)


@ui.page("/")
async def home():
    with ui.card().classes("w-full"):
        code_editor = (
            CodeMirror()
            # .on(
            #    "change",
            #    lambda e: ui.notify(f"The value changed to {e.args['value']}."),
            # )
            # .on("focus", lambda e: ui.notify(f"The editor got focus."))
            # .on("blur", lambda e: ui.notify(f"The editor lost focus."))
        )

        ui.textarea().bind_value(code_editor, "value")

        result = ui.label()
        ui.button("execute python code").on(
            "click", lambda: cbackhand(code_editor.value, result)
        )


ui.run()
