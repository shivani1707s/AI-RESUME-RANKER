import pandas as pd
from tqdm import tqdm

from src.read_job import read_job_description
from src.data.load_data import load_candidates
from src.data.preprocess import extract_candidate
from src.data.text_builder import build_candidate_text

from src.models.embeddings import model
from src.models.semantic_match import calculate_similarity

from src.models.ranking import (
    experience_score,
    skills_score,
    profile_score,
    github_score,
    response_score,
    open_to_work_score,
    final_score,
)


def extract_required_skills(job_text):
    """
    TODO:
    Replace with proper extraction from job description.
    """
    return [
        "python",
        "sql",
        "machine learning",
        "deep learning",
        "nlp",
    ]


def extract_required_experience(job_text):
    """
    TODO:
    Replace with regex/LLM extraction.
    """
    return 3


def main():

    print("=" * 60)
    print("Reading Job Description...")
    print("=" * 60)

    job_text = read_job_description()

    required_skills = extract_required_skills(job_text)
    required_experience = extract_required_experience(job_text)

    print("Loading Candidates...")

    df = load_candidates()

    print("Number of Candidates:", len(df))

    print("Generating Job Embedding...")

    job_embedding = model.encode(
        job_text,
        convert_to_numpy=True
    )

    results = []

    print("Ranking Candidates...\n")

    for _, row in tqdm(df.iterrows(), total=len(df)):

        candidate = extract_candidate(row)

        candidate_text = build_candidate_text(candidate)

        candidate_embedding = model.encode(
            candidate_text,
            convert_to_numpy=True
        )

        semantic = calculate_similarity(
            job_embedding,
            candidate_embedding
        )

        exp = experience_score(
            candidate["years_experience"],
            required_experience
        )

        skills = skills_score(
            candidate["skills"],
            required_skills
        )

        profile = profile_score(
            candidate["profile_score"]
        )

        github = github_score(
            candidate["github_score"]
        )

        response = response_score(
            candidate["response_rate"]
        )

        open_work = open_to_work_score(
            candidate["open_to_work"]
        )

        score = final_score(
            semantic,
            skills,
            exp,
            profile,
            github,
            response,
            open_work
        )

        results.append(
            {
                "candidate_id": candidate["candidate_id"],
                "semantic_score": round(semantic, 4),
                "skills_score": round(skills, 4),
                "experience_score": round(exp, 4),
                "profile_score": round(profile, 4),
                "github_score": round(github, 4),
                "response_score": round(response, 4),
                "open_to_work_score": round(open_work, 4),
                "final_score": round(score, 4),
            }
        )

    result_df = pd.DataFrame(results)

    result_df = result_df.sort_values(
        by="final_score",
        ascending=False
    )

    result_df.insert(
        0,
        "rank",
        range(1, len(result_df) + 1)
    )

    output_file = "outputs/final_rankings.csv"

    result_df.to_csv(
        output_file,
        index=False
    )

    print("\nDone!")
    print(result_df.head(10))
    print(f"\nSaved to {output_file}")


if __name__ == "__main__":
    main()