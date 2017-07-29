
import winshell


recycle_bin = winshell.recycle_bin()
recycle_bin.empty(confirm=False, show_progress=False, sound=True)