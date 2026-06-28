def get_performance_category(score):
    if score < 50:
        return "Poor"
    elif score <= 75:
        return "Average"
    else:
        return "Good"


def generate_suggestions(study_hours, attendance, sleep_hours, previous_score, assignments):
    suggestions = []

    if study_hours < 4:
        suggestions.append("Increase study hours for better performance.")

    if attendance < 75:
        suggestions.append("Improve attendance.")

    if sleep_hours < 6:
        suggestions.append("Sleep at least 7 hours.")

    if assignments < 5:
        suggestions.append("Complete more assignments.")

    if previous_score < 60:
        suggestions.append("Revise basics regularly.")

    return suggestions