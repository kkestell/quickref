```python
import urwid

# ----------------------------------------------------------------------------
# Simple Text Display
# ----------------------------------------------------------------------------

text = urwid.Text("Hello, World!")
filler = urwid.Filler(text, "top")
loop = urwid.MainLoop(filler)
loop.run()


# ----------------------------------------------------------------------------
# Simple List Display
# ----------------------------------------------------------------------------

body = [
    urwid.Text("Item 1"),
    urwid.Divider(),
    urwid.Text("Item 2"),
    urwid.Divider(),
    urwid.Text("Item 3"),
]

listbox = urwid.ListBox(urwid.SimpleListWalker(body))
filler = urwid.Filler(listbox, "top")
loop = urwid.MainLoop(filler)
loop.run()


# ----------------------------------------------------------------------------
# Simple Button
# ----------------------------------------------------------------------------

def on_button_click(button):
    text.set_text("Button clicked!")

button = urwid.Button("Click me!")
urwid.connect_signal(button, "click", on_button_click)
filler = urwid.Filler(button, "middle")
loop = urwid.MainLoop(filler)
loop.run()


# ----------------------------------------------------------------------------
# Simple Edit Field
# ----------------------------------------------------------------------------

def on_edit_change(edit, new_text):
    text.set_text(f"You typed: {new_text}")

edit = urwid.Edit("Type here: ")
urwid.connect_signal(edit, "change", on_edit_change)
filler = urwid.Filler(edit, "middle")
loop = urwid.MainLoop(filler)
loop.run()


# ----------------------------------------------------------------------------
# Simple Pop-up Dialog Box
# ----------------------------------------------------------------------------

def on_yes_button_click(button):
    text.set_text("You clicked 'Yes'")

def on_no_button_click(button):
    text.set_text("You clicked 'No'")

yes_button = urwid.Button("Yes", on_yes_button_click)
no_button = urwid.Button("No", on_no_button_click)
buttons = urwid.GridFlow([yes_button, no_button], 10, 3, 1, "center")

dialog = urwid.LineBox(urwid.Pile([
    urwid.Text("Do you like Python?"),
    urwid.Divider(),
    buttons,
]))

filler = urwid.Filler(dialog, "middle")
loop = urwid.MainLoop(filler)
loop.run()

# ----------------------------------------------------------------------------
# Simple Tree Display
# ----------------------------------------------------------------------------

tree = urwid.TreeWalker(urwid.ParentNode([
    urwid.TreeNode("Item 1", [
        urwid.TreeNode("Subitem 1.1"),
        urwid.TreeNode("Subitem 1.2"),
    ]),
    urwid.TreeNode("Item 2", [
        urwid.TreeNode("Subitem 2.1"),
        urwid.TreeNode("Subitem 2.2"),
    ]),
]))

treebox = urwid.TreeBox(tree)
filler = urwid.Filler(treebox, "top")
loop = urwid.MainLoop(filler)
loop.run()


# ----------------------------------------------------------------------------
# Simple Grid Display
# ----------------------------------------------------------------------------

grid = urwid.GridFlow([
    urwid.Text("Item 1"),
    urwid.Text("Item 2"),
    urwid.Text("Item 3"),
], 10, 3, 1, "center")

filler = urwid.Filler(grid, "top")
loop = urwid.MainLoop(filler)
loop.run()


# ----------------------------------------------------------------------------
# Simple Frame with Padding
# ----------------------------------------------------------------------------

frame = urwid.Frame(urwid.Text("Hello, World!"))
padding = urwid.Padding(frame, "center", width="pack")
filler = urwid.Filler(padding, "top")
loop = urwid.MainLoop(filler)
loop.run()


# ----------------------------------------------------------------------------
# Simple LineBox
# ----------------------------------------------------------------------------

linebox = urwid.LineBox(urwid.Text("Hello, World!"))
filler = urwid.Filler(linebox, "top")
loop = urwid.MainLoop(filler)
loop.run()


# ----------------------------------------------------------------------------
# Custom Signals and Handlers
# ----------------------------------------------------------------------------

class CustomButton(urwid.Button):
    signals = ["custom_click"]

    def __init__(self, label, on_custom_click=None):
        super().__init__(label)

        if on_custom_click is not None:
            urwid.connect_signal(self, "custom_click", on_custom_click)

    def keypress(self, size, key):
        if key == "c":
            self._emit("custom_click")
        else:
            return super().keypress(size, key)

def on_custom_click(button):
    text.set_text("Custom button clicked!")

button = CustomButton("Click me!", on_custom_click)
filler = urwid.Filler(button, "middle")
loop = urwid.MainLoop(filler)
loop.run()
```