"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    Parameters:
        student_scores (list[float]): Student exam scores.

    Returns:
        list[int]: Student scores *rounded* to the nearest integer value.
    """

    rounded_scores = [ round(round_score) for round_score in student_scores]
    return rounded_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    Parameters:
        student_scores (list[int]): Student scores as ints.

    Returns:
        int: The count of student scores at or below 40.
    """
    failing_count = len([score for score in student_scores if score<=40])
    return failing_count


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    Parameters:
        student_scores (list[int]): Integer scores.
        threshold (int): The threshold to cross to be the "best" score.

    Returns:
        list[int]: Integer scores that are at or above the "best" threshold.
    """
    scores_above_threshold = [ score for score in student_scores if score>=threshold]
    return scores_above_threshold


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    Parameters:
        highest (int): The value of the highest exam score.

    Returns:
        list[int]: Lower threshold scores for each D-A letter grade interval.

        For example, where the highest score is 100, and failing is <= 40,
        The result would be [41, 56, 71, 86]:
            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    sub = 0
    if highest>97 and highest<= 100:
        sub = 15
    elif highest >95 and highest<=97:
        sub = 14
    elif highest > 85 and highest<=95:
        sub = 13
    elif highest >82 and highest<=85:
        sub=11
    else:
        sub= 10

    grade_scr = []
    for idx in range(0,4):
        if idx ==0:
            grade_scr.append(41)
        else:
            grade_scr.append(grade_scr[idx-1]+sub)
    return grade_scr

    


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    Parameters:
        student_scores (list): Scores in descending order.
        student_names (list[str]): Student names by exam score in descending order.

    Returns:
        list[str]: Strings in format ["<rank>. <student name>: <score>"].
    """
    student_ranks= []
    for idx in range(0,len(student_scores)):
        student_ranks.append(f"{idx+1}. {student_names[idx]}: {student_scores[idx]}")
    return student_ranks
    


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    Parameters:
        student_info (list[list[str, int]]): List of [<student name>, <score>] lists.

    Returns:
        list: First `[<student name>, 100]` found OR `[]` if no student score of 100 is found.
    """
    perfect_score_queue = [prft_scr for prft_scr in student_info if prft_scr[-1]==100]
    if len(perfect_score_queue)==0:
        return []
    return perfect_score_queue[0]