# CARA Classifier — Curavolv Phase 1 Assessment

A rule-based candidate profile classifier that recommends the best-fit healthcare graduate degree and career tracks based on a candidate's academic background, statement of purpose, and personal strengths.

---

## What This Project Does

Given a candidate profile in JSON format, the classifier outputs:
- **Recommended Degree** — one of MHA, MPH, MSHI, or MBA-HC
- **Top 3 Career Tracks** — ranked by fit score
- **Rationale** — a short explanation for each recommendation

---

## How It Works

The classifier uses a **weighted scoring system** across three signals:

### 1. Subject Scoring
Each subject in the candidate's academic background is mapped to a subject cluster (C1–C10). Each cluster awards points to relevant degrees.

```
Example:
"anatomy" → C1 (Life Sciences) → MPH +2, MSHI +1
"python"  → C7 (IT)            → MSHI +3, MBA-HC +1
```

### 2. SOP Keyword Scoring
The candidate's Statement of Purpose is scanned for domain keywords. Each keyword awards points to relevant career tracks and degrees.

```
Example:
"quality improvement" → T01 (Administration) +3, MHA +2
"ehr"                 → T09 (Digital Health)  +3, MSHI +3
```

### 3. Strengths Bonus
Each personal strength awards a small bonus to the most aligned degree.

```
Example:
"Leadership" → MHA +1
"Curiosity"  → MSHI +1, MPH +1
```

### Final Decision
- **Degree** → whichever degree has the highest total score wins
- **Tracks** → top 3 tracks by score are selected; if fewer than 3 tracks scored, degree-aligned backup tracks fill the remaining slots

---

## Project Structure

```
cara_classifier/
├── candidates.json     # Input — all 6 candidate profiles
├── classifier.py       # Core logic — scoring, ranking, rationale
├── main.py             # Entry point — runs classifier, saves output
└── results.json        # Output — generated after running main.py
```

---

## Degrees Classified

| Degree | Full Name | Focus Area |
|--------|-----------|------------|
| MHA | Master of Health Administration | Provider operations, hospital leadership |
| MPH | Master of Public Health | Population health, epidemiology, policy |
| MSHI | Master of Science in Health Informatics | Health IT, data systems, EHR |
| MBA-HC | MBA with Healthcare Concentration | Finance, strategy, entrepreneurship |

---

## Career Tracks

| ID | Track Name |
|----|------------|
| T01 | Healthcare Administration, Operations, Quality & Risk |
| T02 | Healthcare Consulting & Advisory |
| T03 | Healthcare Finance, Payer Strategy & Value-Based Care |
| T04 | Behavioral Health & Human Services Management |
| T05 | Public, Community & Global Health Programs |
| T06 | Population Health Analytics, Epidemiology & Outcomes Research |
| T07 | Health Policy, Economics & Advocacy |
| T08 | Environmental, Occupational & Climate Health |
| T09 | Digital Health, Informatics & Data Governance |
| T10 | Life Sciences, Clinical Research & Regulatory Management |
| T11 | Healthcare Entrepreneurship, Product & Innovation |

---

## How to Run

### Requirements
- Python 3.7 or above
- No external libraries needed — uses only Python built-ins

### Steps

```bash
# Step 1 — Clone or download the project folder
cd cara_classifier

# Step 2 — Run the classifier
python main.py

# Step 3 — View results
# Results are printed to the terminal and saved to results.json
```

---

## Sample Output

```json
{
  "candidate_id": "Sample_FreshGrad_01",
  "recommended_degree": "MHA",
  "degree_scores": {
    "MHA": 20,
    "MPH": 18,
    "MSHI": 8,
    "MBA-HC": 1
  },
  "top_career_tracks": [
    {
      "rank": 1,
      "track_id": "T01",
      "track_name": "Healthcare Administration, Operations, Quality & Risk",
      "score": 9,
      "rationale": "Candidate's SOP directly mentions 'administrative leadership' and 'quality improvement', which strongly signals this track."
    },
    {
      "rank": 2,
      "track_id": "T02",
      "track_name": "Healthcare Consulting & Advisory",
      "score": 0,
      "rationale": "Secondary fit based on MHA degree alignment and leadership strengths."
    },
    {
      "rank": 3,
      "track_id": "T04",
      "track_name": "Behavioral Health & Human Services Management",
      "score": 0,
      "rationale": "Tertiary recommendation based on MHA degree pathway and adjacent career option."
    }
  ]
}
```

---

## Test Candidates & Results Summary

| Candidate | Background | Recommended Degree | Primary Track |
|-----------|------------|-------------------|---------------|
| Sample_FreshGrad_01 | BDS — Dental Surgery | MHA | T01 — Healthcare Administration |
| Sample_MPH_Community_01 | BA Sociology | MPH | T05 — Community & Global Health |
| Sample_MBA_Finance_01 | BCom Accounting & Finance | MBA-HC | T03 — Healthcare Finance |
| Sample_MSHI_Tech_01 | BTech Computer Science | MSHI | T09 — Digital Health & Informatics |
| Sample_MHA_LTC_01 | BSc Nursing | MHA | T01 — Healthcare Administration |
| Sample_MPH_Policy_01 | BA Political Science | MPH | T07 — Health Policy & Advocacy |

---

## Key Design Decisions

**Rule-based over ML** — The classifier uses a deterministic weighted scoring system rather than a machine learning model. This makes the logic fully transparent, explainable, and easy to audit — which is important for a candidate evaluation pipeline.

**Holistic scoring** — Degree fit is treated as a weighted signal across subjects, SOP, and strengths rather than a hard gate. A candidate with a clinical background but a strong finance-oriented SOP will reflect that cross-boundary evidence in their scores.

**Backup track system** — When SOP keywords alone do not generate 3 scored tracks, the classifier falls back to degree-aligned default tracks to ensure a complete recommendation in all cases.

---

## AI/LLM Usage Disclosure

As required by the submission guidelines, here is a transparent account of AI tool usage in this project:

- **Claude (Anthropic)** was used as a learning aid to understand the architecture approach and explain Python concepts during development.
- All scoring weights, keyword maps, cluster mappings, and design decisions were defined manually by the author based on the provided rubric.
- All code was written and understood by the author. AI was not used to generate the submission on the author's behalf.

---

## Author

**Abdullah Khan**
Curavolv AI & Software Development Internship — Phase 1 Assessment
