#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the winning Monday-morning joke to /output/entry.txt."""
import os

LINE = "Monday morning is the weekend's eviction notice: Sunday night it knocks politely; by 7 a.m. it has changed the locks, sublet your pillow to your inbox, and kept the deposit."


def main() -> None:
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
