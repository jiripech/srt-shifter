#!/usr/bin/env python3
import argparse
from datetime import datetime, timedelta
from pathlib import Path
import sys


def parse_timestamp(text: str) -> datetime:
    try:
        return datetime.strptime(text, "%H:%M:%S,%f")
    except ValueError as exc:
        raise ValueError(f"Invalid timestamp format: {text}") from exc


def format_timestamp(dt: datetime) -> str:
    return dt.strftime("%H:%M:%S,%f")[:-3]


def shift_srt(filename: Path, shift_ms: int) -> Path:
    if not filename.exists():
        raise FileNotFoundError(f"Input file does not exist: {filename}")

    shift_delta = timedelta(milliseconds=shift_ms)
    target = filename.with_name(f"{filename.stem}.shifted{filename.suffix}")

    data = []
    for line in filename.read_text(encoding="utf-8").splitlines():
        if "-->" in line:
            left, right = [x.strip() for x in line.split("-->", 1)]
            start = parse_timestamp(left) + shift_delta
            end = parse_timestamp(right) + shift_delta
            data.append(f"{format_timestamp(start)} --> {format_timestamp(end)}")
        else:
            data.append(line)

    target.write_text("\n".join(data) + "\n", encoding="utf-8")
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description="Shift SRT subtitles by given milliseconds")
    parser.add_argument("filename", help="Path to input SRT file")
    parser.add_argument("shift_ms", type=int, help="Shift amount in milliseconds (negative allowed)")
    args = parser.parse_args()

    try:
        src = Path(args.filename)
        out = shift_srt(src, args.shift_ms)
        print(f"Created shifted file: {out}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
