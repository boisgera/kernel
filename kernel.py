import ast
import os

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
        with open("input", "r") as input_fifo:
            data = input_fifo.read()
            print(f"-> {data}")
            if data:
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
                print(f"-> {repr(out)}")
                with open("output", "w") as output_fifo:
                    output_fifo.write(repr(out))

if __name__ == "__main__":
    main()
