# ================= ATS SCORE =================

@app.route("/ats_score", methods=["POST"])
@login_required
def ats_score():
    letter = session.get("letter", "").lower()
    jd = request.form["jd"].lower()

    jd_words = set(jd.replace(",", "").replace(".", "").split())
    letter_words = set(letter.replace(",", "").replace(".", "").split())

    ignore_words = {"the", "and", "is", "at", "on", "a", "an", "to", "for", "with", "in", "of"}

    jd_keywords = {word for word in jd_words if word not in ignore_words and len(word) > 3}

    matched = jd_keywords.intersection(letter_words)
    missing = jd_keywords - letter_words

    score = int((len(matched) / len(jd_keywords)) * 100) if jd_keywords else 0

    return render_template("ats.html",
                           score=score,
                           matched=sorted(list(matched)),
                           missing=sorted(list(missing)))