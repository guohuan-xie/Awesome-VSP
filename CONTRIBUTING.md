# Contributing

Thanks for helping improve Awesome Video Scene Parsing.

## Add Or Update A Paper

1. Edit `data/papers.csv`.
2. Use `NA` for unknown code or project links.
3. Keep task names to one of: `VSS`, `VIS`, `VPS`, `VTS`, `OVVS`, `Unified`, `Future`.
4. Regenerate the README:

```bash
python3 scripts/generate_readme.py
```

## Entry Format

Each entry should include:

- `task`: task family.
- `year`: publication year.
- `venue`: venue or preprint source.
- `method`: short method name used in the survey.
- `title`: full paper title.
- `paper_url`: paper, project, arXiv, open-access, or Scholar link.
- `code_url`: implementation link when available.
- `project_url`: project/demo page when available.
- `tags`: semicolon-separated method tags.
- `note`: short one-line description.

## Scope

This repository prioritizes methods discussed in the companion VSP survey. Closely related datasets, benchmarks, and unified segmentation systems are welcome when they clarify the survey taxonomy.
