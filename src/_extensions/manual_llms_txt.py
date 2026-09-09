import subprocess
import sys
from pathlib import Path


def generate_llms_txt(app, exception):
    if exception is not None or app.builder.name != "html":
        return

    source_root = Path(app.srcdir).parent
    subprocess.run(
        (sys.executable, source_root / "scripts" / "generate_llms_txt.py"),
        cwd=Path(app.outdir).parent,
        check=True,
    )


def setup(app):
    app.connect("build-finished", generate_llms_txt)
    return {"parallel_read_safe": True, "parallel_write_safe": True}