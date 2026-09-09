import re
from pathlib import Path


# The bundled Sphinx Book theme emits this icon without an alt attribute.
BINDER_IMAGE_PATTERN = re.compile(
    r'<img\b(?![^>]*\s+alt\s*=)(?=[^>]*\s+src\s*=\s*["\'][^"\']*logo_binder\.svg["\'])[^>]*>',
    re.IGNORECASE,
)


def add_binder_alt_text(app, exception):
    if exception is not None:
        return

    for html_path in Path(app.outdir).rglob("*.html"):
        html = html_path.read_text(encoding="utf-8")
        updated_html = BINDER_IMAGE_PATTERN.sub(_with_decorative_alt, html)
        if updated_html != html:
            html_path.write_text(updated_html, encoding="utf-8")


def _with_decorative_alt(match):
    image_tag = match.group(0)
    closing_tag = "/>" if image_tag.endswith("/>") else ">"
    return f'{image_tag[: -len(closing_tag)].rstrip()} alt="Binder"{closing_tag}'


def setup(app):
    app.connect("build-finished", add_binder_alt_text)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
