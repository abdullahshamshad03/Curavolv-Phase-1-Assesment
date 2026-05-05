import json
from classifier import classify

with open("candidates.json", "r") as f:
    candidates = json.load(f)


all_results = []

for candidate in candidates:
   
    result = classify(candidate)
    all_results.append(result)


print("RESULTS")
print("\n")

for result in all_results:
    print(f"\n Candidate  : {result['candidate_id']}")
    print(f" Degree     : {result['recommended_degree']}")
    print(f" Scores     : {result['degree_scores']}")
    print(" Top Tracks :")
    for track in result["top_career_tracks"]:
        print(f"   #{track['rank']} {track['track_id']} — {track['track_name']} (Score: {track['score']})")



with open("results.json", "w") as f:
    json.dump(all_results, f, indent=2)

print("The result has been saved in results.json file")
