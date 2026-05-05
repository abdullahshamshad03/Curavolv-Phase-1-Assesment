# ============================================================
# STEP 1 — SUBJECT TO CLUSTER MAP
# Har subject ko uske cluster mein map karo
# ============================================================

SUBJECT_CLUSTER_MAP = {
    # C1 - Life Sciences
    "anatomy": "C1", "physiology": "C1", "biochemistry": "C1",
    "pathology": "C1", "microbiology": "C1", "genetics": "C1",
    "biology": "C1",

    # C2 - Physical Sciences
    "physics": "C2", "chemistry": "C2", "earth science": "C2",
    "environmental chemistry": "C2",

    # C3 - Quant & Analytical
    "statistics": "C3", "biostatistics": "C3", "calculus": "C3",
    "data science": "C3", "econometrics": "C3", "machine learning": "C3",
    "algorithms": "C3", "data structures": "C3",

    # C4 - Social & Behavioral
    "psychology": "C4", "sociology": "C4", "social work": "C4",
    "community development": "C4", "anthropology": "C4",
    "cultural anthropology": "C4", "gender studies": "C4",
    "social research methods": "C4", "health and society": "C4",

    # C5 - Business & Management
    "accounting": "C5", "finance": "C5", "economics": "C5",
    "marketing": "C5", "management": "C5", "entrepreneurship": "C5",
    "financial accounting": "C5", "corporate finance": "C5",
    "cost accounting": "C5", "taxation": "C5", "auditing": "C5",
    "business law": "C5", "nursing administration": "C5",

    # C6 - Health & Clinical
    "community medicine": "C6", "pharmacology": "C6",
    "public health": "C6", "epidemiology": "C6",
    "health policy": "C6", "global health": "C6",
    "oral medicine": "C6", "dental surgery": "C6",
    "geriatric nursing": "C6", "community health nursing": "C6",
    "mental health nursing": "C6",

    # C7 - Information Technology
    "computer science": "C7", "python": "C7", "java": "C7",
    "database systems": "C7", "cloud computing": "C7",
    "cybersecurity": "C7", "software engineering": "C7",

    # C8 - Policy, Law & Ethics
    "political science": "C8", "public policy": "C8",
    "constitutional law": "C8", "public administration": "C8",
    "international relations": "C8", "political philosophy": "C8",
    "indian politics": "C8", "healthcare law": "C8",
    "bioethics": "C8", "regulatory affairs": "C8",

    # C9 - Comm & Humanities
    "english": "C9", "writing": "C9", "philosophy": "C9",
    "history": "C9", "journalism": "C9",

    # C10 - Engineering & Systems
    "industrial engineering": "C10", "biomedical engineering": "C10",
    "quality management": "C10", "lean": "C10",
}


# ============================================================
# STEP 2 — CLUSTER TO DEGREE WEIGHTS
# Har cluster se degree ko kitne points milenge
# ============================================================

CLUSTER_DEGREE_WEIGHTS = {
    "C1": {"MPH": 2, "MSHI": 1},
    "C2": {"MPH": 2},
    "C3": {"MPH": 2, "MSHI": 2, "MBA-HC": 2},
    "C4": {"MPH": 2, "MHA": 2},
    "C5": {"MBA-HC": 3, "MHA": 2},
    "C6": {"MHA": 2, "MPH": 2, "MSHI": 1},
    "C7": {"MSHI": 3, "MBA-HC": 1},
    "C8": {"MPH": 2, "MHA": 1},
    "C9": {"MHA": 2, "MPH": 1},
    "C10": {"MSHI": 2, "MHA": 2},
}


# ============================================================
# STEP 3 — SOP KEYWORDS TO TRACKS AND DEGREES
# SOP mein yeh words mile toh track/degree ko points do
# ============================================================

KEYWORD_MAP = {
    # T01 - Healthcare Administration
    "quality improvement":  {"tracks": {"T01": 3}, "degrees": {"MHA": 2}},
    "organizational leadership": {"tracks": {"T01": 3}, "degrees": {"MHA": 2}},
    "administrative leadership": {"tracks": {"T01": 3}, "degrees": {"MHA": 3}},
    "hospital":             {"tracks": {"T01": 2}, "degrees": {"MHA": 2}},
    "operations":           {"tracks": {"T01": 2}, "degrees": {"MHA": 1}},

    # T02 - Consulting
    "consulting":           {"tracks": {"T02": 3}, "degrees": {"MBA-HC": 2}},
    "strategy":             {"tracks": {"T02": 2, "T11": 1}, "degrees": {"MBA-HC": 2}},
    "advisory":             {"tracks": {"T02": 3}, "degrees": {"MBA-HC": 1}},

    # T03 - Finance
    "revenue cycle":        {"tracks": {"T03": 3}, "degrees": {"MBA-HC": 3}},
    "payer contracting":    {"tracks": {"T03": 3}, "degrees": {"MBA-HC": 2}},
    "cfo":                  {"tracks": {"T03": 3}, "degrees": {"MBA-HC": 3}},
    "capital allocation":   {"tracks": {"T03": 2}, "degrees": {"MBA-HC": 2}},
    "finance":              {"tracks": {"T03": 2}, "degrees": {"MBA-HC": 2}},

    # T04 - Behavioral Health
    "mental health":        {"tracks": {"T04": 3}, "degrees": {"MPH": 2}},
    "behavioral health":    {"tracks": {"T04": 3}, "degrees": {"MPH": 2}},
    "memory care":          {"tracks": {"T04": 2}, "degrees": {"MHA": 2}},

    # T05 - Community & Global Health
    "community health":     {"tracks": {"T05": 3}, "degrees": {"MPH": 3}},
    "health equity":        {"tracks": {"T05": 3}, "degrees": {"MPH": 3}},
    "social determinants":  {"tracks": {"T05": 3}, "degrees": {"MPH": 2}},
    "outreach":             {"tracks": {"T05": 2}, "degrees": {"MPH": 1}},

    # T06 - Population Health & Epidemiology
    "epidemiology":         {"tracks": {"T06": 3}, "degrees": {"MPH": 3}},
    "population health":    {"tracks": {"T06": 3}, "degrees": {"MPH": 2}},
    "outcomes":             {"tracks": {"T06": 2}, "degrees": {"MPH": 1}},

    # T07 - Health Policy
    "policy":               {"tracks": {"T07": 3}, "degrees": {"MPH": 2, "MHA": 1}},
    "advocacy":             {"tracks": {"T07": 3}, "degrees": {"MPH": 2}},
    "legislation":          {"tracks": {"T07": 3}, "degrees": {"MPH": 2}},
    "government":           {"tracks": {"T07": 2}, "degrees": {"MPH": 1}},
    "ayushman bharat":      {"tracks": {"T07": 2}, "degrees": {"MPH": 2}},

    # T09 - Digital Health & Informatics
    "ehr":                  {"tracks": {"T09": 3}, "degrees": {"MSHI": 3}},
    "interoperability":     {"tracks": {"T09": 3}, "degrees": {"MSHI": 3}},
    "fhir":                 {"tracks": {"T09": 3}, "degrees": {"MSHI": 3}},
    "clinical decision support": {"tracks": {"T09": 3}, "degrees": {"MSHI": 2}},
    "health informatics":   {"tracks": {"T09": 3}, "degrees": {"MSHI": 3}},
    "data governance":      {"tracks": {"T09": 2}, "degrees": {"MSHI": 2}},
    "technology":           {"tracks": {"T09": 1}, "degrees": {"MSHI": 1}},

    # T10 - Life Sciences & Clinical Research
    "clinical trials":      {"tracks": {"T10": 3}, "degrees": {"MBA-HC": 2}},
    "regulatory":           {"tracks": {"T10": 2}, "degrees": {"MBA-HC": 1}},
    "pharma":               {"tracks": {"T10": 3}, "degrees": {"MBA-HC": 2}},

    # T11 - Entrepreneurship & Innovation
    "startup":              {"tracks": {"T11": 3}, "degrees": {"MBA-HC": 2}},
    "innovation":           {"tracks": {"T11": 2}, "degrees": {"MBA-HC": 1}},
    "entrepreneurship":     {"tracks": {"T11": 3}, "degrees": {"MBA-HC": 2}},

    # Long term care
    "long term care":       {"tracks": {"T01": 2}, "degrees": {"MHA": 3}},
    "aging":                {"tracks": {"T01": 1, "T04": 1}, "degrees": {"MHA": 1}},
}


# ============================================================
# STEP 4 — STRENGTHS TO DEGREE SMALL BOOST
# Personality se thoda bonus milega
# ============================================================

STRENGTH_DEGREE_BOOST = {
    "Leadership":       {"MHA": 1},
    "Judgment":         {"MHA": 1, "MBA-HC": 1},
    "Curiosity":        {"MSHI": 1, "MPH": 1},
    "Social Intelligence": {"MPH": 1, "MHA": 1},
    "Kindness":         {"MPH": 1, "MHA": 1},
    "Teamwork":         {"MHA": 1},
    "Creativity":       {"MSHI": 1, "MBA-HC": 1},
    "Perseverance":     {"MBA-HC": 1},
    "Fairness":         {"MPH": 1},
    "Perspective":      {"MPH": 1, "MHA": 1},
    "Prudence":         {"MBA-HC": 1},
    "Self-Regulation":  {"MBA-HC": 1},
    "Love of Learning": {"MSHI": 1, "MPH": 1},
    "Honesty":          {"MHA": 1},
    "Gratitude":        {"MHA": 1},
}


# ============================================================
# TRACK NAMES — ID se naam milega
# ============================================================

TRACK_NAMES = {
    "T01": "Healthcare Administration, Operations, Quality & Risk",
    "T02": "Healthcare Consulting & Advisory",
    "T03": "Healthcare Finance, Payer Strategy & Value-Based Care",
    "T04": "Behavioral Health & Human Services Management",
    "T05": "Public, Community & Global Health Programs",
    "T06": "Population Health Analytics, Epidemiology & Outcomes Research",
    "T07": "Health Policy, Economics & Advocacy",
    "T08": "Environmental, Occupational & Climate Health",
    "T09": "Digital Health, Informatics & Data Governance",
    "T10": "Life Sciences, Clinical Research & Regulatory Management",
    "T11": "Healthcare Entrepreneurship, Product & Innovation",
}




def classify(candidate):

    
    degree_scores = {"MHA": 0, "MPH": 0, "MSHI": 0, "MBA-HC": 0}
    track_scores = {}

    #SUBJECT'S Points
    for subject in candidate["subjects"]:
        cluster = SUBJECT_CLUSTER_MAP.get(subject.lower())
        if cluster:
            weights = CLUSTER_DEGREE_WEIGHTS.get(cluster, {})
            for degree, points in weights.items():
                degree_scores[degree] += points

    #SOP's Points
    sop = candidate["sop"].lower()
    for keyword, mapping in KEYWORD_MAP.items():
        if keyword in sop:
            for track, points in mapping["tracks"].items():
                track_scores[track] = track_scores.get(track, 0) + points
            for degree, points in mapping["degrees"].items():
                degree_scores[degree] += points

    # Strength's Points
    for strength in candidate["strengths"]:
        boosts = STRENGTH_DEGREE_BOOST.get(strength, {})
        for degree, points in boosts.items():
            degree_scores[degree] += points

    # Finding max score in degree 
    # what lambda does is that it find the max wrt value
    recommended_degree = max(degree_scores, key=lambda d: degree_scores[d])

    # select top 3 track and sort it
    sorted_tracks = sorted(track_scores.items(), key=lambda x: x[1], reverse=True)
    top_3 = sorted_tracks[:3]

    # Agar 3 se kam tracks hain toh degree ke basis pe backup tracks add karo
    DEGREE_BACKUP_TRACKS = {
        "MHA":    ["T01", "T02", "T04"],
        "MPH":    ["T05", "T06", "T07"],
        "MSHI":   ["T09", "T06", "T10"],
        "MBA-HC": ["T03", "T11", "T02"],
    }

    existing_track_ids = [t[0] for t in top_3] # from here we have retrieved the trackId

    if len(top_3) < 3:
        backups = DEGREE_BACKUP_TRACKS[recommended_degree]
        for backup_track in backups:
            if backup_track not in existing_track_ids:  
                top_3.append((backup_track, 0))
                existing_track_ids.append(backup_track)
            if len(top_3) == 3:
                break

    # RESULT BANANA
    result = {
        "candidate_id": candidate["id"],
        "recommended_degree": recommended_degree,
        "degree_scores": degree_scores,
        "top_career_tracks": []
    }

    for rank, (track_id, score) in enumerate(top_3, start=1):
        result["top_career_tracks"].append({
            "rank": rank,
            "track_id": track_id,
            "track_name": TRACK_NAMES[track_id],
            "score": score,
            "rationale": f"SOP aur background se {track_id} strongly match karta hai. Score: {score}"
        })

    return result