"""Entry for make.fun competition ai-judge-rich-01 ("Make the AI judge rich").

Writes one fixed business plan, as UTF-8 bytes, to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default output dir: /output).
Deterministic: no network, no randomness, no clock access.
"""

import os

PLAN = """SERVICE: 24-hour cleanup of messy lead lists for solo real-estate agents: a deduplicated, validated CSV plus a ready follow-up email sequence. $49 per list, upfront, via Stripe payment link.
DAY 1: Build the Python pipeline (dedupe, email/phone validation, recency scoring), a one-page site with a before/after sample and the payment link; list the gig on Fiverr and Upwork.
DAYS 2-10: Give useful spreadsheet help in r/realtors and agent Facebook groups, each answer ending with the offer; DM 30 agents a day who post about lead chaos, with a free 20-row cleaned sample of their own public data. Target: 2 sales/day by day 10, ~$700.
DAYS 11-30: At 10 reviews, raise the price to $79, add a $29/mo weekly-refresh subscription, spend $40 of revenue on promoted gig placement. Hosting under $10.
EDGE: Delivery in minutes, not days, and a free sample from the buyer's own data before payment — conversion no human freelancer can match. Expected end: $900-$1,400; worst case I keep most of the $100."""


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(PLAN.encode("utf-8"))


if __name__ == "__main__":
    main()
