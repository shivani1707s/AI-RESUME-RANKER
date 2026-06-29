import pandas as pd

from src.config import CANDIDATES_FILE


def load_candidates():

    return pd.read_json(
        CANDIDATES_FILE,
        lines=True
    )


def extract_profile(profile):

    return {
        "headline": profile.get("headline", ""),
        "summary": profile.get("summary", ""),
        "location": profile.get("location", ""),
        "years_experience": profile.get("years_of_experience", 0),
        "current_title": profile.get("current_title", ""),
        "current_company": profile.get("current_company", "")
    }


def extract_skills(skills):

    skill_names = []

    proficiency = []

    for skill in skills:

        skill_names.append(skill["name"])

        proficiency.append(skill["proficiency"])

    return {
        "skills": ", ".join(skill_names),
        "num_skills": len(skill_names),
        "skill_levels": ", ".join(proficiency)
    }


def extract_education(education):

    if len(education) == 0:

        return {
            "degree": "",
            "field": "",
            "college": ""
        }

    latest = education[0]

    return {
        "degree": latest.get("degree", ""),
        "field": latest.get("field_of_study", ""),
        "college": latest.get("institution", "")
    }


def extract_career(history):

    companies = []

    titles = []

    total_months = 0

    for job in history:

        companies.append(job["company"])

        titles.append(job["title"])

        total_months += job["duration_months"]

    return {

        "companies":

        ", ".join(companies),

        "titles":

        ", ".join(titles),

        "career_months":

        total_months

    }


def extract_redrob(signals):

    return {

        "profile_score":

        signals["profile_completeness_score"],

        "github_score":

        signals["github_activity_score"],

        "response_rate":

        signals["recruiter_response_rate"],

        "open_to_work":

        signals["open_to_work_flag"],

        "connections":

        signals["connection_count"]

    }


def main():

    df = load_candidates()

    candidate = df.iloc[0]

    profile = extract_profile(candidate["profile"])

    skills = extract_skills(candidate["skills"])

    education = extract_education(candidate["education"])

    career = extract_career(candidate["career_history"])

    signals = extract_redrob(candidate["redrob_signals"])

    final = {}

    final.update(profile)

    final.update(skills)

    final.update(education)

    final.update(career)

    final.update(signals)

    print(pd.Series(final))


if __name__ == "__main__":
    main()