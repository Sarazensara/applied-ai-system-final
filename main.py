# Simple AI Music Recommender System

song_database = {
    "happy": ["Happy - Pharrell Williams", "Good as Hell - Lizzo", "Can't Stop the Feeling - Justin Timberlake"],
    "sad": ["Someone Like You - Adele", "All Too Well - Taylor Swift", "Stay - Rihanna"],
    "workout": ["Stronger - Kanye West", "POWER - Kanye West", "Titanium - David Guetta"],
    "chill": ["Sunflower - Post Malone", "Location - Khalid", "Peaches & Cream - Lo-Fi"],
    "romantic": ["Perfect - Ed Sheeran", "All of Me - John Legend", "Best Part - H.E.R."]
}

def recommend_music(user_input):
    user_input = user_input.lower()
    
    for mood in song_database:
        if mood in user_input:
            return song_database[mood]
    
    return ["No clear match found. Try a different mood!"]


# ---- TEST SYSTEM (your AI feature) ----
test_inputs = [
    "happy songs",
    "sad music",
    "workout playlist",
    "chill vibes",
    "romantic songs"
]

def run_tests():
    results = []
    
    for prompt in test_inputs:
        output = recommend_music(prompt)
        
        if "No clear match" in output[0]:
            results.append((prompt, "FAIL"))
        else:
            results.append((prompt, "PASS"))
    
    return results


if __name__ == "__main__":
    print("Sample Run:")
    print(recommend_music("happy songs"))
    
    print("\nTest Results:")
    for result in run_tests():
        print(result)