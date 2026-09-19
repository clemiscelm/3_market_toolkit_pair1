"""
Ingest module — load and clean price data from CSVs.

>>> Partner A owns this module. <<<

Every function below has:
  - a docstring saying WHAT the function should do (the contract)
  - a series of  # TODO  comments saying HOW to do it, step by step
  - a  raise NotImplementedError  as a placeholder — delete it when done

Your job: replace the NotImplementedError with real code, following the TODOs.

You are DONE with this module when this command runs green:

    pytest tests/test_ingest.py -v

Do not edit tests/test_ingest.py — that file defines what "correct" means.
"""

from pathlib import Path
import pandas as pd


def load_prices(path):
    """
    Load ONE price CSV and return a tidy DataFrame.

    The input CSV has 2 columns:
        date   (string, YYYY-MM-DD)
        close  (float)

    Your job: return a DataFrame with 3 columns, IN THIS ORDER:
        date    (datetime, NOT string)
        ticker  (string, taken from the filename without the .csv extension,
                 always LOWERCASE — e.g. 'data/raw/AAPL.csv' → 'aapl')
        close   (float)

    Example:
        >>> df = load_prices('data/raw/aapl.csv')
        >>> list(df.columns)
        ['date', 'ticker', 'close']
        >>> df['ticker'].iloc[0]
        'aapl'

    Parameters
    ----------
    path : str or pathlib.Path
        Path to a single CSV file.

    Returns
    -------
    pandas.DataFrame
    """
    # TODO 1: convert  path  into a Path object so you can use  .stem
    #         (Path('data/raw/aapl.csv').stem  →  'aapl')
    #         >>> path = Path(path)
    path = Path(path)

    # TODO 2: read the CSV with pd.read_csv(path, parse_dates=['date'])
    #         The  parse_dates  argument makes the date column datetime automatically.
    #         >>> df = pd.read_csv(path, parse_dates=['date'])
    df = pd.read_csv(path, parse_dates=['date'])

    # TODO 3: add a 'ticker' column set to  path.stem.lower()
    #         >>> df['ticker'] = path.stem.lower()
    df['ticker'] = path.stem.lower()

    # TODO 4: reorder columns to  ['date', 'ticker', 'close']  and return
    #         >>> return df[['date', 'ticker', 'close']]
    return df[['date', 'ticker', 'close']]


def clean_prices(df):
    """
    Clean a price DataFrame.

    Steps, in order:
      1. Drop rows where  close  is NaN
      2. Sort by  date  ascending
      3. Drop exact duplicate rows
      4. Reset the index (so rows become 0, 1, 2, ...)

    The function must NOT modify the input — return a new DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        Any DataFrame with a  close  column.

    Returns
    -------
    pandas.DataFrame
    """
    # TODO 1: drop NaN closes
    #         HINT:  df.dropna(subset=['close'])

    # TODO 2: sort by date

    # TODO 3: drop duplicates

    # TODO 4: reset the index — pass  drop=True  or the old index becomes a column

    # HINT: you can chain the steps — pandas methods return new DataFrames by default:
    #     return (df.dropna(subset=['close'])
    #               .sort_values('date')
    #               .drop_duplicates()
    #               .reset_index(drop=True))

    raise NotImplementedError("clean_prices — see the TODOs above")


def load_all_prices(folder):
    """
    Load every  *.csv  file in  folder , combine them into ONE DataFrame,
    then clean the result.

    Parameters
    ----------
    folder : str or pathlib.Path
        Folder containing per-ticker CSVs (aapl.csv, msft.csv, ...).

    Returns
    -------
    pandas.DataFrame
        All prices concatenated and cleaned.

    Raises
    ------
    FileNotFoundError
        If  folder  does not exist OR contains no  .csv  files.
    """
    # TODO 1: convert folder to a Path object
    folder = Path(folder)

    # TODO 2: raise FileNotFoundError if the folder doesn't exist
    #         HINT:  if not folder.is_dir(): raise FileNotFoundError(f"...")

    # TODO 3: list the CSV files with  list(folder.glob('*.csv'))
    #         Then raise FileNotFoundError if the list is empty.

    # TODO 4: loop over the files, call  load_prices  on each,
    #         collect the DataFrames in a list.
    #         HINT:
    #             dfs = []
    #             for f in csv_files:
    #                 dfs.append(load_prices(f))

    # TODO 5: combine with  pd.concat(dfs, ignore_index=True)

    # TODO 6: pass the combined DataFrame through  clean_prices  and return the result

    raise NotImplementedError("load_all_prices — see the TODOs above")
