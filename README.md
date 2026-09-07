# Template: template-book

This template provides a boilerplate repository for books in Duckietown.

## What to change

These are the fields you __must__ update to create your book.

### Placeholders in `src/_config.yml`

This file configures the build of the book.
Replace the placeholder string `BOOK_NAME_HERE` (there should be two separate instances of it) with
the name of the repository hosting your book (e.g., `book-devmanual-docs`).

### Structure in `src/_toc.yml`

Use the [Jupyter Book table-of-contents instructions](https://jupyterbook.org/en/stable/structure/toc.html#structure-of-a-book)
to learn how to structure your book using the Table of Contents file `_toc.yml`.
A simple example is already provided by this template. Adapt it to your needs.

### Logo in `src/logo.png`

There is a default logo in `src/logo.png`. This is the book's logo, change it with something that
reflects the scope of your book. Transparent PNGs are recommended.

## Build

You can build this book by running the command,

```shell
dts docs build
```

## Markdown audit

Run the Markdown and MyST audit before building the book:

```shell
python3 scripts/audit_markdown.py
```

To audit a changed page or build after the checks pass:

```shell
python3 scripts/audit_markdown.py --file src/path/to/page.md
python3 scripts/audit_markdown.py --build
python3 scripts/audit_markdown.py --review-unpunctuated
```

The audit runs the pinned Markdownlint version, verifies source-relative `{include}` targets, checks eligible HTML-commented Markdown sections independently, and enforces the Manual's marker, list, and fence-spacing conventions. It requires `npx`; `--build` additionally requires `dts`.
