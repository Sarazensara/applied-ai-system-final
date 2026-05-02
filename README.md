## AI Music Recommender System

This project is an applied AI system that recommends songs based on user mood input. It simulates how AI systems process input, retrieve relevant data, and generate useful outputs.

This project builds on a previous music recommender simulation by improving reliability through testing and evaluation.

---

## AI Feature: Reliability Testing System

This system includes a testing component that evaluates how well the recommender performs across multiple inputs.

The system runs predefined test cases and checks whether valid recommendations are returned.

---

## Architecture Overview

Input → Mood Detection → Song Retrieval → Output → Testing System

---

## Setup Instructions

1. Clone the repository
   git clone https://github.com/Sarazensara/applied-ai-system-final.git

2. Navigate to the project folder
   cd applied-ai-system-final

3. Run the program
   python main.py

---

## Sample Interaction

Input:
happy songs

Output:
["Happy - Pharrell Williams", "Good as Hell - Lizzo", "Can't Stop the Feeling - Justin Timberlake"]

---

## Testing Summary

* Tested 5 inputs
* 5/5 returned valid recommendations
* System performs consistently for known moods

---

## Design Decisions

* Used keyword matching for simplicity
* Focused on reliability rather than complexity
* Trade-off: limited flexibility vs predictable outputs

---

## Reflection & Ethics

* Limitation: system only works for predefined moods
* Bias: recommendations are limited to the dataset
* Misuse: could give repetitive suggestions

AI was helpful in suggesting structure, but sometimes gave overly complex solutions that were simplified for this implementation.

## Loom Video
https://www.loom.com/share/5e5d6956cd6e479e8fbdda6469cff83d