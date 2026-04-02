# Helix Notebook

An interactive Python experience with Helix, the Kitty terminal and IPython.

## Prerequisites

- `uv` package manager
- `kitty` terminal

## Getting Started

Install the dependencies

```sh
uv sync
```

Open a new kitty window

```sh
kitty -o allow_remote_control=yes -o enabled_layouts=tall
```

Inside the new terminal create a split

```sh
kitty @ launch --title python --cwd=current --keep-focus uv run ipython
```

Start working on a Python file!

```sh
hx my_notebook.py
```

Select some text with your mouse or the `x` key. Press `control` `r` to run it in IPython.

You may change the `control` `r` keybind in the `.helix` directory in the repo.
