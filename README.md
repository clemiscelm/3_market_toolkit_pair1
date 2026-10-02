# market-toolkit

A minimal toolkit for loading, cleaning, and computing metrics on financial time series.

Component B of MSA-DATI07-01 · Python Environments and Engineering Workflows.

## Team

<!-- TODO (both partners): add your names below, one line each. -->
<!-- This is one of the shared files — you WILL hit a merge conflict here. That is expected. -->

- Partner A: Clément Bostyn
- Partner B: Clément Morel
- Partner C: Edward Cardona

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

From the project root, run the summary script:

```bash
./scripts/fetch_prices.sh
```

This checks the raw CSV files in `data/raw/`, prints a one-line summary per ticker to the terminal, and writes the same output to `logs/fetch_YYYY-MM-DD.log`.

To generate the cumulative-return chart and print the per-ticker metrics:

```bash
python -m src.demo
```

This reads all price files, prints a summary for each ticker, and saves the chart to `outputs/cumulative_returns.png`.

## Structure

- `data/raw/` — original CSV price data used as the source for ingestion and analysis.
- `src/` — Python modules for loading, cleaning, calculating metrics, and demonstrating the workflow.
- `scripts/` — shell utilities for validating the raw data and writing a daily summary log.
- `tests/` — tests that define the expected behavior for ingestion and metrics calculations.

## Development workflow

Every change goes through a Pull Request. `main` stays green.

1. `git switch -c feature/<your-change>`
2. Do the work, commit as you go
3. Push, open a PR against `main`
4. Your partner reviews. You iterate. You merge when both are happy.
5. Never push directly to `main`.
