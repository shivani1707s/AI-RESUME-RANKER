import pandas as pd

from src.config import CANDIDATES_FILE


def load_candidates():
    """Load the candidates dataset."""
    df = pd.read_json(CANDIDATES_FILE, lines=True)
    return df


def main():
    print("=" * 60)
    print("Loading candidates...")
    print("=" * 60)

    df = load_candidates()

    print(f"Number of candidates : {len(df)}")
    print(f"Number of columns    : {len(df.columns)}")
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst Candidate:")
    print(df.iloc[0])


if __name__ == "__main__":
    main()