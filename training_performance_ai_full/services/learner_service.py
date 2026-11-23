from models.learner_model import (
    LearnerRequest,
    LearnerAnalysis,
    LearnerResponse
)


def analyze_learner(
    request: LearnerRequest
) -> LearnerResponse:

    avg = round(
        (
            request.pythonScore +
            request.sqlScore +
            request.fastapiScore
        ) / 3,
        2
    )

    if avg >= 85:
        level = "Excellent"

    elif avg >= 70:
        level = "Good"

    elif avg >= 50:
        level = "Needs Improvement"

    else:
        level = "Critical Improvement Required"

    scores = {
        "Python": request.pythonScore,
        "SQL": request.sqlScore,
        "FastAPI": request.fastapiScore
    }

    strongest = max(
        scores,
        key=scores.get
    )

    weakest = min(
        scores,
        key=scores.get
    )

    completion = 0

    if request.totalAssignments > 0:

        completion = round(
            (
                request.assignmentsCompleted /
                request.totalAssignments
            ) * 100,
            2
        )

    assessment = (
        f"Strongest area is {strongest}. "
        f"Focus improvement on {weakest}."
    )

    recommendations = []

    if weakest == "SQL":

        recommendations = [
            "SQL Joins",
            "SQL Subqueries",
            "SQL Aggregate Functions"
        ]

    elif weakest == "Python":

        recommendations = [
            "Python OOP",
            "Exception Handling",
            "File Handling"
        ]

    else:

        recommendations = [
            "FastAPI Routing",
            "Pydantic Models",
            "API Validation"
        ]

    final_recommendation = (
        "Continue learning and project practice."
    )

    if request.attendancePercentage < 75:

        final_recommendation = (
            "Improve attendance and maintain learning consistency."
        )

    if completion < 70:

        final_recommendation = (
            "Complete more assignments before advancing to next modules."
        )

    analysis = LearnerAnalysis(

        averageScore=avg,

        performanceLevel=level,

        strongestTechnology=strongest,

        weakestTechnology=weakest,

        technicalAssessment=assessment,

        recommendedLearning=recommendations
    )

    return LearnerResponse(

        learnerName=request.learnerName,

        department=request.department,

        analysis=analysis,

        finalRecommendation=final_recommendation
    )