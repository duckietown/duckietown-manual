```{seo}
:description: Learn how to compile Duckietown project documentation with Jupyter Book, mix Markdown with reStructuredText, and optionally autogenerate API docs.
:keywords: Duckietown, documentation, Jupyter Book, Sphinx, eval‑rst, API docs, dts docs build
```
(sec:dt_way_build_docs)=
# Building Code Documentation

```{needget}
* [Book‑writer manual](book-devmanual-intro)
---
* Ability to build and preview a Jupyter Book for your project
```

Duckietown projects ship with a ready‑to‑use Jupyter Book skeleton under **`/docs/src`**. Refer to the [Book Writer Manual](book-devmanual-intro) for details on the supported features and a syntax cheat sheet.


## Quick build command

From the project root:

```bash
dts docs build
```

`dts` launches a container, resolves dependencies, and writes the rendered HTML to **`/docs/html`**.


## Mixing reStructuredText inside Markdown

MyST supports the [`{eval-rst}` directive](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html), enabling adding raw rST blocks in a `.md` file — useful when requiring constructs that Markdown lacks.


## Automatic API generation *(advanced)*

Sphinx can parse docstrings and create an API reference automatically.

To enable this:

1. Add [`sphinx.ext.autodoc`](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) and, if desired, `autodoc_typehints` to `docs/src/conf.py`.

2. Create stub files (e.g., `reference/api.rst`) that call `.. automodule::` or `.. autofunction::`.

3. Re‑run `dts docs build`.

See the *Developers* section of the [official Jupyter Book guide](https://jupyterbook.org/en/stable/advanced/developers.html) for detailed instructions.

