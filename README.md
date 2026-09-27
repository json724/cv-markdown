# cv-markdown

Personal project to track changes in my CV and LinkedIn profile.

- `json_cv_2026.md` / `.pdf`: current CV, plain Markdown built for ATS parsers (single column, no images, no tables, ASCII only).
- `build.sh`: renders a CV to PDF (`./build.sh json_cv_2026.md`, needs pandoc and google-chrome); styles in `build/cv.css`.
- `tools/ats_check.py`: simulates an ATS read of the PDF (extraction, contact, sections, positions, keyword match). Run `uv run --script tools/ats_check.py json_cv_2026.pdf keywords.txt` with one keyword per line from the job posting.
- `linkedin_profile.md`: headline, About and current-role text for LinkedIn.
- `archive/`: the 2025 CV and the old QR code.
