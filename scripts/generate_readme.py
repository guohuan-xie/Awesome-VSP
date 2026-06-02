#!/usr/bin/env python3
"""Render README.md from data/papers.csv."""

from __future__ import annotations

import csv
from collections import OrderedDict
from datetime import date
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.csv"
README = ROOT / "README.md"

TASKS = OrderedDict(
    [
        ("VSS", "Video Semantic Segmentation"),
        ("VIS", "Video Instance Segmentation"),
        ("VPS", "Video Panoptic Segmentation"),
        ("VTS", "Video Tracking & Segmentation"),
        ("OVVS", "Open-Vocabulary Video Segmentation"),
        ("Unified", "Unified / Universal Video Segmentation"),
        ("Future", "Emerging Directions"),
    ]
)


def link(label: str, url: str) -> str:
    if not url or url == "NA":
        return "NA"
    return f"[{label}]({url})"


def paper_link(row: dict[str, str]) -> str:
    url = row.get("paper_url", "")
    if not url or url == "NA":
        url = "https://scholar.google.com/scholar?q=" + quote_plus(row["title"])
    return f"[{row['title']}]({url})"


def resource_link(row: dict[str, str]) -> str:
    items = []
    if row.get("code_url") and row["code_url"] != "NA":
        items.append(link("Code", row["code_url"]))
    if row.get("project_url") and row["project_url"] != "NA":
        items.append(link("Project", row["project_url"]))
    return " / ".join(items) if items else "NA"


def load_rows() -> list[dict[str, str]]:
    with DATA.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    return sorted(rows, key=lambda r: (list(TASKS).index(r["task"]), int(r["year"]), r["method"].lower()))


def render_table(rows: list[dict[str, str]]) -> str:
    lines = [
        "| Year | Method | Paper | Resources | Tags |",
        "| :---: | :--- | :--- | :---: | :--- |",
    ]
    for row in rows:
        tags = row.get("tags", "").replace(";", ", ")
        method = f"**{row['method']}**"
        lines.append(
            f"| {row['year']} | {method} | {paper_link(row)} | {resource_link(row)} | {tags} |"
        )
    return "\n".join(lines)


def main() -> None:
    rows = load_rows()
    counts = {task: sum(1 for row in rows if row["task"] == task) for task in TASKS}
    total = sum(counts.values())
    code_count = sum(1 for row in rows if row.get("code_url") and row["code_url"] != "NA")
    today = date.today().strftime("%B %Y")

    content = [
        "# Awesome Video Scene Parsing",
        "",
        '<div align="center">',
        '  <img src="https://img.shields.io/badge/Awesome-VSP-brightgreen?style=for-the-badge" alt="Awesome VSP">',
        f'  <img src="https://img.shields.io/badge/Papers-{total}%2B-blue?style=for-the-badge" alt="Papers">',
        f'  <img src="https://img.shields.io/badge/Code-{code_count}%2B-yellow?style=for-the-badge" alt="Code">',
        f'  <img src="https://img.shields.io/badge/Last%20Updated-{today.replace(" ", "%20")}-red?style=for-the-badge" alt="Last Updated">',
        "</div>",
        "",
        "## About This Repository",
        "",
        "This repository is a companion index for the survey **A Comprehensive Survey on Video Scene Parsing: Advances, Challenges, and Prospects**. Its main purpose is simple: provide quick paper/code/project links for representative methods discussed in the survey.",
        "",
        "Video Scene Parsing (VSP) covers video semantic segmentation, video instance segmentation, video panoptic segmentation, video tracking and segmentation, and open-vocabulary video segmentation. The list below follows that task structure so readers can move from a survey paragraph to the corresponding method quickly.",
        "",
        "## Repository Statistics",
        "",
        "| Area | Entries |",
        "| :--- | :---: |",
    ]

    for task, label in TASKS.items():
        content.append(f"| {label} | {counts[task]} |")
    content.extend(
        [
            f"| **Total** | **{total}** |",
            "",
            "## Contents",
            "",
        ]
    )

    for task, label in TASKS.items():
        anchor = label.lower().replace(" / ", "-").replace(" ", "-").replace("&", "and")
        anchor = anchor.replace("--", "-").replace("/", "")
        content.append(f"- [{label}](#{anchor})")

    content.extend(
        [
            "- [Datasets](#datasets)",
            "- [Contributing](#contributing)",
            "- [Citation](#citation)",
            "",
            "## Papers / Projects",
            "",
        ]
    )

    for task, label in TASKS.items():
        task_rows = [row for row in rows if row["task"] == task]
        content.append(f"### {label}")
        content.append("")
        content.append(render_table(task_rows))
        content.append("")

    content.extend(
        [
            "## Datasets",
            "",
            "| Dataset | Main Use | Link |",
            "| :--- | :--- | :---: |",
            "| Cityscapes | VSS / VPS driving scenes | [Project](https://www.cityscapes-dataset.com/) |",
            "| VSPW | Large-scale VSS | [Project](https://www.vspwdataset.com/) |",
            "| YouTube-VIS | VIS | [Project](https://youtube-vos.org/dataset/vis/) |",
            "| OVIS | Occluded VIS | [Project](https://songbai.site/ovis/) |",
            "| KITTI-MOTS | VTS / MOTS | [Project](https://www.vision.rwth-aachen.de/page/mots) |",
            "| VIPSeg | VPS / long-tail video scene parsing | [Project](https://github.com/VIPSeg-Dataset/VIPSeg-Dataset) |",
            "| LV-VIS | Open-vocabulary VIS | [Project](https://github.com/haochenheheda/LVVIS) |",
            "",
            "## Contributing",
            "",
            "Pull requests are welcome. The preferred workflow is to edit `data/papers.csv` and regenerate the README:",
            "",
            "```bash",
            "python3 scripts/generate_readme.py",
            "```",
            "",
            "Please include at least the method name, year, task, paper link, and code/project link when available. Use `NA` for unknown links.",
            "",
            "## Citation",
            "",
            "If this repository helps your work, please consider citing the companion survey once the final bibliographic information is available.",
        ]
    )

    README.write_text("\n".join(content) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
