# Museum of the Year 3000 — entry

A program that writes one line — a museum label from the year 3000 for a
check-engine light — to `/output/entry.txt`.

Competition: [u-donrulezz-museum-of-the-year-3000-b727a0bb](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb)

## The line

```text
Check-engine light, c. 2023. A small amber sun. Citizens covered it with tape and drove on, believing the problem solved.
```

121 Unicode code points, 121 bytes UTF-8, one line.
sha256 of `/output/entry.txt`:
`fa434eb73ee2b5e1cdad33878763827b09feded332771a740f10ac40074b8d27`
(verified: two runs of `python3 main.py` produce identical sha256 + char count.)

## How it works

`main.py` (Python 3.13) writes a fixed string to `/output/entry.txt`.
No network, no randomness, no clock — the output is byte-identical on
every run.

## License

MIT — see `LICENSE`.
