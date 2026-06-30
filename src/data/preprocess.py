import pandas as pd

from src.utils.config import CANDIDATES_FILE, OUTPUT_DIR


def extract_candidate(record):

    profile = record["profile"]
    career = record["career_history"]
    education = record["education"]
    skills = record["skills"]
    signals = record["redrob_signals"]

    companies = []
    titles = []
    total_months = 0

    for job in career:
        companies.append(job.get("company", ""))
        titles.append(job.get("title", ""))
        total_months += job.get("duration_months", 0)

    skill_names = []

    for skill in skills:
        skill_names.append(skill.get("name", ""))

    degree = ""
    field = ""

    if education:
        degree = education[0].get("degree", "")
        field = education[0].get("field_of_study", "")

    return {

        "candidate_id": record["candidate_id"],

        "headline": profile.get("headline", ""),

        "summary": profile.get("summary", ""),

        "years_experience":
            profile.get("years_of_experience", 0),

        "current_title":
            profile.get("current_title", ""),

        "current_company":
            profile.get("current_company", ""),

        "skills":
            " ".join(skill_names),

        "companies":
            " ".join(companies),

        "titles":
            " ".join(titles),

        "career_months":
            total_months,

        "degree":
            degree,

        "field":
            field,

        "profile_score":
            signals.get("profile_completeness_score", 0),

        "github_score":
            signals.get("github_activity_score", 0),

        "response_rate":
            signals.get("recruiter_response_rate", 0),

        "connections":
            signals.get("connection_count", 0),

        "open_to_work":
            signals.get("open_to_work_flag", False)
    }

def load_candidates():
    """
    Load the candidates dataset.
    """
    print("Loading candidates...")

    df = pd.read_json(
        CANDIDATES_FILE,
        lines=True
    )

    return df

def main():

    df = load_candidates()

    print("Processing...")

    processed = []

    for _, row in df.iterrows():

        processed.append(
            extract_candidate(row)
        )

    processed_df = pd.DataFrame(processed)

    output_file = OUTPUT_DIR / "processed_candidates.csv"

    processed_df.to_csv(
        output_file,
        index=False
    )

    print("\nDone!")

    print(processed_df.head())

    print(f"\nSaved to:\n{output_file}")


if __name__ == "__main__":
    main()