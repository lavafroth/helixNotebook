import code
import os
import sys

pipe = ".notebook"

try:
    os.mkfifo(pipe)
except OSError as e:
    e.add_note("Error creating named pipe: .notebook")
    e.add_note("Consider removing the stale session's .notebook file")
    raise

interpreter = code.InteractiveConsole()
try:
    with open(pipe) as handle:
        while True:
            for line in handle:
                interpreter.push(line)
except FileNotFoundError as e:
    e.add_note("Named pipe no longer exists")
    raise
except OSError as e:
    e.add_note("Error reading from named pipe")
    raise
except KeyboardInterrupt:
    if os.path.exists(pipe):
        os.unlink(pipe)
    sys.exit()
