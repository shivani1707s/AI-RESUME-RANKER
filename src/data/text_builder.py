def build_candidate_text(candidate):

    text = f"""
    {candidate['headline']}

    {candidate['summary']}

    Skills:
    {candidate['skills']}

    Companies:
    {candidate['companies']}

    Roles:
    {candidate['titles']}

    Experience:
    {candidate['years_experience']} years

    Degree:
    {candidate['degree']}
    """

    return text.strip()