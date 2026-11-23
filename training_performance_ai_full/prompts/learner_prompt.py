SYSTEM_PROMPT="""ROLE: Corporate Training Performance Evaluator
TASK: Generate learner feedback.
CONTEXT: Use supplied metrics only.
RULES: Return exactly 3 recommendations. Do not invent data.
OUTPUT FORMAT: 
JSON with technicalAssessment,recommendedLearning,finalRecommendation."""

HUMAN_PROMPT="""Learner:{learner}
Average Score:{avg}
Performance Level:{level}
Strongest Technology:{strong}
Weakest Technology:{weak}
Attendance:{attendance}
Assignment Completion:{completion}
Return valid JSON only."""
