"""Create disposable projects for the intake behavioral scenarios."""

import json
import tempfile
from pathlib import Path


def main():
    cases = json.loads(Path(__file__).with_name("cases.json").read_text())
    root = Path(tempfile.mkdtemp(prefix="skulls-evals-"))
    for case in cases:
        project = root / case["id"]
        project.mkdir()
        for relative_path, content in case["files"].items():
            target = project / relative_path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content)
        print(f"{case['id']}: {project}")
    print("Prompts and checks: evals/cases.json")


if __name__ == "__main__":
    main()
