import gui
import core
import utils

gui.assembleButton.configure(command=core.assemble)
gui.file_menu.add_command(label="Open", command=utils.open_file)
gui.file_menu.add_command(label="Save", command=utils.save_file)
gui.file_menu.add_separator()
gui.file_menu.add_command(label="Exit", command=gui.window.quit)

gui.window.bind('<Control-r>', lambda _: core.assemble())
gui.window.bind('<Control-o>', lambda _: utils.open_file())
gui.window.bind('<Control-s>', lambda _: utils.save_file())
gui.window.bind('<Control-n>', lambda _: gui.asmEditor.delete("1.0", "end"))
gui.window.bind('<Control-R>', lambda _: core.assemble())
gui.window.bind('<Control-O>', lambda _: utils.open_file())
gui.window.bind('<Control-S>', lambda _: utils.save_file())
gui.window.bind('<Control-N>', lambda _: core.asmEditor.delete("1.0", "end"))

gui.window.mainloop()