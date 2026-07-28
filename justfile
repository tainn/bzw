alias f := fix
alias s := sync

# command list
default:
    @just --list --unsorted

# astral lint && fmt && check
fix:
    ruff check bzw
    ruff format bzw
    ty check bzw

# astral lib sync
sync:
    uv sync
