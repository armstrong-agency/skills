"""Repository checks for a public skills repo: privacy patterns, code blocks, relative links."""
import json, pathlib, re, sys, tomllib

ROOT = pathlib.Path(__file__).resolve().parents[2]
HEX_ID = re.compile(r"\b[0-9a-f]{24}\b")
LOCAL_PATH = re.compile(r"/Users/|/home/[a-z]|[A-Z]:\\Users\\")
BLOCK = re.compile(r"```(toml|json)\n(.*?)```", re.S)
LINK = re.compile(r"\]\(([^)\s#]+)(#[^)]*)?\)")

errors = []
for md in sorted(ROOT.rglob("*.md")):
    if ".git" in md.parts:
        continue
    rel = md.relative_to(ROOT)
    text = md.read_text(encoding="utf-8")
    for n, line in enumerate(text.splitlines(), 1):
        if HEX_ID.search(line):
            errors.append(f"{rel}:{n}: looks like a Webflow site or workspace ID")
        if LOCAL_PATH.search(line):
            errors.append(f"{rel}:{n}: local filesystem path")
    for lang, body in BLOCK.findall(text):
        body = re.sub(r"\{[a-z-]+\}", "x", body) if lang == "toml" else body
        try:
            tomllib.loads(body) if lang == "toml" else json.loads(body)
        except Exception as e:
            errors.append(f"{rel}: invalid {lang} block: {e}")
    for target, _ in LINK.findall(text):
        if re.match(r"[a-z]+:", target):
            continue
        if not (md.parent / target).exists():
            errors.append(f"{rel}: broken link {target}")

print("\n".join(errors) or "All checks passed.")
sys.exit(1 if errors else 0)
