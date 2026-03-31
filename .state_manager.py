from pathlib import Path
from sys import argv
state = Path(".state")

if len(argv) < 2:
    exit()

cell_path = Path(argv[1])

state_bytes = 0

if state.exists():
    state_bytes = state.read_bytes()
    state_bytes = int.from_bytes(state_bytes) + 1
state.write_bytes(state_bytes.to_bytes())

save_path = cell_path.with_stem(cell_path.stem + '_' + str(state_bytes))
cell_path.rename(save_path)

