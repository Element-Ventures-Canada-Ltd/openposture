# Handling: Unclassified — public
# SPDX-License-Identifier: Apache-2.0
"""Build the turbopump viewer with its data embedded.

  python3 tools/build_ui.py                      -> ui/turbopump.html and ui/map.html (standalone, public facts)
  python3 tools/build_ui.py --page map --fragment OUT.html   -> one page, body only
  python3 tools/build_ui.py --fragment OUT.html  -> page body only (for hosting inside another shell)
  python3 tools/build_ui.py --overlay O.json --fragment OUT.html
        -> adds a private working view; O.json must stay outside this repository
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "engine"))
import public_facts  # noqa: E402
import turbopump  # noqa: E402

DOC = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
       '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n{body}\n</html>\n')


PAGES = {"turbopump": ("turbopump.template.html", "Turbopump Supply Map", "Turbopump Working View"),
         "map": ("map.template.html", "Canada Space Supply Chain Map", "Canada Space Supply Chain Map · Working View")}


def build(overlay=None, page_name="turbopump", working_js=""):
    tpl_name, title, wtitle = PAGES[page_name]
    data = {"tp": turbopump.facts(*turbopump.load()),
            "trace": public_facts.facts(public_facts.load(ROOT / "examples" / "synthetic-turbopump-thread.yaml"))}
    if overlay:
        data["overlay"] = overlay
    tpl = (ROOT / "ui" / tpl_name).read_text(encoding="utf-8")
    blob = json.dumps(data, ensure_ascii=False, default=str).replace("</", "<\\/")
    page = tpl.replace("/*__DATA__*/null", blob)
    # Working-view code is a private add-in (kept outside this repository) and is injected only
    # into overlay builds. Public builds carry no engine-derived logic.
    page = page.replace("/*__WORKING_JS__*/", working_js if overlay else "")
    if overlay:
        page = page.replace("Handling: Unclassified — public (public build). SPDX-License-Identifier: Apache-2.0",
                            overlay["handling"]).replace(f"<title>{title}</title>", f"<title>{wtitle}</title>")
    return page


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--overlay")
    ap.add_argument("--fragment")
    ap.add_argument("--page", default="turbopump", choices=sorted(PAGES))
    ap.add_argument("--working-js", help="private add-in for overlay builds")
    a = ap.parse_args()
    ov = json.loads(Path(a.overlay).read_text(encoding="utf-8")) if a.overlay else None
    if a.fragment:
        wjs = Path(a.working_js).read_text(encoding="utf-8") if a.working_js else ""
        Path(a.fragment).write_text(build(ov, a.page, wjs), encoding="utf-8")
    else:
        if ov:
            sys.exit("refusing to write an overlay build into the repository")
        for name in PAGES:
            (ROOT / "ui" / f"{name}.html").write_text(DOC.format(body=build(None, name)), encoding="utf-8")
