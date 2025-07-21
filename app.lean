
def eval (code: String) : IO String := do
    IO.FS.writeFile "input" code
    return (<- IO.FS.readFile "output")

def exec (code: String) : IO Unit := do
    IO.FS.writeFile "input" code
    let _ <- IO.FS.readFile "output"
    return ()

def import_ (module : String) : IO Unit :=
    exec s!"from {module} import *"

def init_window (width: Nat) (height: Nat) (title : String) : IO Unit := do
    let code := s!"init_window({width}, {height}, \"{title}\")"
    exec code

def window_should_close : IO Bool := do
    let status <- eval "window_should_close()"
    return status == "True"

def set_target_fps (fps : Nat) : IO Unit :=
    exec s!"set_target_fps({fps})"

def begin_drawing : IO Unit := exec "begin_drawing()"

def end_drawing : IO Unit := exec "end_drawing()"

abbrev Color := List Nat

def clear_background (color : Color) : IO Unit :=
    exec s!"clear_background({color})"


def draw_text (text : String) (x : Nat) (y : Nat) (fontSize : Nat) (color : Color) : IO Unit :=
    exec s!"draw_text(\"{text}\", {x}, {y}, {fontSize}, {color})"

def close_window : IO Unit := exec "close_window()"

def WHITE := [255, 255, 255, 255]

def VIOLET := [135, 60, 190, 255]

def main : IO Unit := do
    import_ "pyray"
    init_window 800 450 "Hello"
    set_target_fps 60
    while not (<- window_should_close) do
        begin_drawing
        clear_background WHITE
        draw_text "Hello world" 190 200 20 VIOLET
        end_drawing
    close_window
