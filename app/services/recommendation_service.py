from store.memory import jobs_seed

def get_recommendations(user: dict):
    recommendations = []
    for job in jobs_seed:
        score = 0

        # 1. Industry match
        if job["industry"].lower() == user["industry"].lower():
            score += 0.5

        # 2. Keyword overlap
        keyword_overlap = len(set(user["keywords"]) & set(job["keywords"]))
        score += 0.1 * keyword_overlap  # each matching keyword +0.1

        # 3. Description similarity (optional simple check)
        desc_words_user = set(user["description"].lower().split())
        desc_words_job = set(job["description"].lower().split())
        common_words = len(desc_words_user & desc_words_job)
        score += 0.01 * common_words

        # Keep score between 0 and 1
        score = min(score, 1)
        recommendations.append({"job_id": job["id"], "score": round(score, 2)})

    # Sort descending by score
    recommendations.sort(key=lambda x: x["score"], reverse=True)
    return recommendations
