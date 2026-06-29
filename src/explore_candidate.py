import json
import pandas as pd

from src.config import CANDIDATES_FILE


def main():

    df = pd.read_json(
        CANDIDATES_FILE,
        lines=True
    )

    candidate = df.iloc[0]

    print("=" * 80)
    print("Candidate ID")
    print("=" * 80)

    print(candidate["candidate_id"])

    print("\n")

    print("=" * 80)
    print("PROFILE")
    print("=" * 80)

    print(json.dumps(candidate["profile"], indent=4))

    print("\n")

    print("=" * 80)
    print("CAREER HISTORY")
    print("=" * 80)

    print(json.dumps(candidate["career_history"], indent=4))

    print("\n")

    print("=" * 80)
    print("EDUCATION")
    print("=" * 80)

    print(json.dumps(candidate["education"], indent=4))

    print("\n")

    print("=" * 80)
    print("SKILLS")
    print("=" * 80)

    print(json.dumps(candidate["skills"], indent=4))

    print("\n")

    print("=" * 80)
    print("CERTIFICATIONS")
    print("=" * 80)

    print(json.dumps(candidate["certifications"], indent=4))

    print("\n")

    print("=" * 80)
    print("LANGUAGES")
    print("=" * 80)

    print(json.dumps(candidate["languages"], indent=4))

    print("\n")

    print("=" * 80)
    print("REDROB SIGNALS")
    print("=" * 80)

    print(json.dumps(candidate["redrob_signals"], indent=4))


if __name__ == "__main__":
    main()