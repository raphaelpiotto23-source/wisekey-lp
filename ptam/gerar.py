#!/usr/bin/env python3
"""Gera os PDFs do PTAM a partir dos HTMLs e numera as páginas.

Uso:
    python3 gerar.py                 # gera todos
    python3 gerar.py relacao-documentos-ptam.html

Requer Chrome ou Chromium no PATH (ou em CHROME_BIN) e:
    pip install pypdf reportlab
"""

import io
import os
import shutil
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent

# Cinza da paleta Wisekey, usado na numeração de página.
CINZA = (0.373, 0.357, 0.470)


def achar_chrome():
    candidatos = [
        os.environ.get("CHROME_BIN"),
        "/opt/pw-browsers/chromium",
        "chromium",
        "chromium-browser",
        "google-chrome",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    ]
    for c in candidatos:
        if not c:
            continue
        caminho = shutil.which(c) or (c if Path(c).exists() else None)
        if caminho:
            return caminho
    sys.exit("Chrome/Chromium não encontrado. Defina CHROME_BIN.")


def html_para_pdf(html: Path, pdf: Path):
    subprocess.run(
        [
            achar_chrome(),
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf}",
            html.as_uri(),
        ],
        check=True,
        capture_output=True,
    )


def numerar(pdf: Path):
    from pypdf import PdfReader, PdfWriter
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.pdfgen import canvas

    leitor = PdfReader(str(pdf))
    total = len(leitor.pages)
    escritor = PdfWriter()

    for i, pagina in enumerate(leitor.pages, start=1):
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=A4)
        c.setFont("Helvetica", 7)
        c.setFillColorRGB(*CINZA)
        c.drawRightString(190 * mm, 8 * mm, f"Página {i} de {total}")
        c.save()
        buf.seek(0)
        pagina.merge_page(PdfReader(buf).pages[0])
        escritor.add_page(pagina)

    with open(pdf, "wb") as f:
        escritor.write(f)
    return total


def main():
    alvos = [Path(a).resolve() for a in sys.argv[1:]] or sorted(BASE.glob("*.html"))
    for html in alvos:
        pdf = html.with_suffix(".pdf")
        html_para_pdf(html, pdf)
        paginas = numerar(pdf)
        print(f"{pdf.name} — {paginas} página(s)")


if __name__ == "__main__":
    main()
