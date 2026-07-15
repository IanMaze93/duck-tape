## Duck-Tape

<img width="1254" height="1254" alt="image" src="https://github.com/user-attachments/assets/07db5ba3-5833-472c-a699-55906b1a6f6c" />

<img width="835" height="561" alt="image" src="https://github.com/user-attachments/assets/dec08c57-7d89-428a-bd49-86f555b92321" />

## This Repo is for personal CLI scripts to ease development

# Getting Started

## Install dependencies

```bash
poetry install
```

## Install Git hooks

```bash
poetry run pre-commit install
```

---

# Development

Run the CLI:

```bash
poetry run duck-tape
```

Run the test suite:

```bash
poetry run pytest
```

Run linting:

```bash
poetry run ruff check .
```

Format the project:

```bash
poetry run ruff format .
```

Run all pre-commit hooks:

```bash
poetry run pre-commit run --all-files
```

## Setup Executable

```bas
poetry run duck-tape setup
```
