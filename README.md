# SRT Shifter

A tiny command line utility to shift `.srt` subtitle timestamps forwards or backwards by a specified number of milliseconds.

## Features

- Parses standard SRT timecode lines (`HH:MM:SS,mmm --> HH:MM:SS,mmm`)
- Applies positive or negative millisecond shift
- Writes output to `input.shifted.srt` (same directory as source)
- Preserves all non-timecode lines (index and text content)

## Requirements

- Python 3.6+

## Usage

From repository root:

```bash
./bin/shift-subtitle.py path/to/subtitles.srt 1500
```

- `path/to/subtitles.srt`: input SRT file
- `1500`: shift in milliseconds (`-1500` to move earlier)

Output example:

- Input: `movie.srt`
- Output: `movie.shifted.srt`

## Example

```bash
./bin/shift-subtitle.py dialogue.srt -500
# created shifted file dialogue.shifted.srt
```

## Development

Make script executable if needed:

```bash
chmod +x bin/shift-subtitle.py
```

## License

See [LICENSE.md](LICENSE.md) for license details.
