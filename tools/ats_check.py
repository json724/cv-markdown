# /// script
# dependencies = ["pypdf", "pdfminer.six"]
# ///
"""Simulate how an ATS reads a CV PDF.

Usage:
  uv run --script tools/ats_check.py json_cv_2026.pdf [keywords.txt]

keywords.txt: one keyword or phrase per line, copied from the job posting.
Without it, a sample list for an AI Engineering Lead role is used.
"""
import re
import sys

from pdfminer.high_level import extract_text
from pypdf import PdfReader

SAMPLE_KEYWORDS = [
    "LLM", "large language model", "generative AI", "agents", "agentic", "RAG", "retrieval",
    "prompt engineering", "fine-tuning", "evaluation", "MLOps", "LLMOps", "Python", "FastAPI",
    "Kubernetes", "Docker", "GCP", "AWS", "microservices", "distributed systems", "system design",
    "architecture", "technical leadership", "mentoring", "stakeholders", "A/B test",
    "vector database", "embeddings", "PyTorch", "transformers", "NLP", "production", "scalability",
    "latency", "CI/CD", "MCP", "LangChain", "LangGraph", "observability", "SQL",
]
STANDARD_SECTIONS = {"SUMMARY", "EXPERIENCE", "SKILLS", "EDUCATION", "CERTIFICATIONS"}
DATES = re.compile(r"^(?:[A-Z][a-z]{2} )?(\d{4}) - (?:[A-Z][a-z]{2} )?(\d{4}|Present)")


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def main():
    pdf = sys.argv[1]
    keywords = SAMPLE_KEYWORDS
    if len(sys.argv) > 2:
        keywords = [k.strip() for k in open(sys.argv[2], encoding="utf-8") if k.strip()]

    t1 = "\n".join(p.extract_text() for p in PdfReader(pdf).pages)
    t2 = extract_text(pdf)
    lines = [l.strip() for l in t2.splitlines() if l.strip()]

    print("1) Extraction")
    print(f"   pypdf and pdfminer agree: {norm(t1) == norm(t2)} ({len(norm(t2))} chars)")
    print(f"   non-ASCII characters: {sorted({c for c in t2 if ord(c) > 127}) or 'none'}")

    print("2) Contact")
    email = re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", t2)
    phone = re.search(r"\+\d[\d ]{8,}\d", t2)
    linkedin = re.search(r"linkedin\.com/in/\S+", t2)
    print(f"   name: {lines[0]}")
    print(f"   email: {email and email.group()} | phone: {phone and phone.group()} | linkedin: {linkedin and linkedin.group()}")

    print("3) Sections")
    for h in (l for l in lines[1:] if l.isupper() and len(l) < 45):
        print(f"   {h:45s} {'standard' if h in STANDARD_SECTIONS else 'free text'}")

    print("4) Positions")
    for i, l in enumerate(lines[:-1]):
        m = DATES.match(lines[i + 1])
        if " | " in l and m:
            title, company = (x.strip() for x in l.split(" | ", 1))
            print(f"   {title[:45]:45s} @ {company[:38]:38s} {m.group(1)}-{m.group(2)}")

    print("5) Keywords")
    low = norm(t2).lower()
    hit = [k for k in keywords if k.lower() in low]
    miss = [k for k in keywords if k.lower() not in low]
    print(f"   match {len(hit)}/{len(keywords)} ({100 * len(hit) // len(keywords)}%)")
    print(f"   missing: {', '.join(miss) or 'none'}")


if __name__ == "__main__":
    main()
