# market-toolkit

A minimal toolkit for loading, cleaning, and computing metrics on financial time series.

Component B of MSA-DATI07-01 · Python Environments and Engineering Workflows.

## Team

<!-- TODO (both partners): add your names below, one line each. -->
<!-- This is one of the shared files — you WILL hit a merge conflict here. That is expected. -->

- Partner A: Clément Bostyn
- Partner B: _name of partner_
- Partner C: _name of partner_

## Setup

From a fresh clone, run the following commands from a terminal. Python 3.11 or
newer is required.

```bash
git clone <repository-url>
cd 3_market_toolkit_pair1
python -m venv .venv
.venv\Scripts\Activate.ps1 # On windows
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
#for mac: python3 -m venv venv  
#for mac: source venv/bin/activate
```

After activation, verify the installation with:

```bash
python -m pytest tests/ -v
```

## How to run

<!-- TODO (Partner B): describe how to run  scripts/fetch_prices.sh  and  src/demo.py . -->
<!-- Include what output files each command produces. -->

## Structure

<!-- TODO (both): describe what each folder is for. Keep it short — 1 line each. -->

- `data/raw/` — original CSV price data kept unchanged as the source for ingestion and analysis.
- `src/` — Python source code for loading, cleaning, analyzing, and demonstrating the price data.
- `scripts/` —
- `tests/` —

## Development workflow

Every change goes through a Pull Request. `main` stays green.

1. `git switch -c feature/<your-change>`
2. Do the work, commit as you go
3. Push, open a PR against `main`
4. Your partner reviews. You iterate. You merge when both are happy.
5. Never push directly to `main`.
