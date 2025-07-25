import ast
import os

def count_open_files():
    fd_dir = '/proc/self/fd'
    try:
        # List all entries in /proc/self/fd — each is an open file descriptor
        fds = os.listdir(fd_dir)
        return fds
    except Exception as e:
        print(f"Error reading {fd_dir}: {e}")
        return None

def main():
    try:
        input = os.mkfifo("input")
    except FileExistsError:
        pass
    try:
       output = os.mkfifo("output")
    except FileExistsError:
        pass

    while True:
        #print(f"Opened files: {count_open_files()}")
        with open("input", "r") as input_fifo:
            data = input_fifo.read()
        if data == "":
            print("EOF")
            continue
        print(f"<- {data}")
        try:
            ast.parse(data, mode="eval")
            out = eval(data, globals())
        except Exception:
            try:
                ast.parse(data, mode="exec")
                exec(data, globals())
                out = None
            except Exception as error:
                out = f"{type(error).__name__}: {error}"
        with open("output", "w") as output_fifo:
            output_fifo.write(repr(out))
            output_fifo.flush()
        print(f"-> {repr(out)}")


if __name__ == "__main__":
    main()
