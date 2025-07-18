def max_seven_day_streak(steps):
    """
    Find the maximum total steps in any 7-day streak.

    Args:
        steps (list[int]): daily step counts.

    Returns:
        tuple[int, int]: maximum sum, starting index of the streak.
    """
    streak = 7
    n = len(steps)

    if n < streak:
        return None, None

    window_sum = sum(steps[:streak])
    max_sum = window_sum
    max_start = 0

    for i in range(streak, n):
        window_sum += steps[i] - steps[i-streak]
        if window_sum > max_sum:
            max_sum = window_sum
            max_start = i - streak + 1

    return max_sum, max_start


def min_three_day_streak(steps):
    """
    Find the minimum total steps in any 3-day streak.

    Args:
        steps (list[int]): daily step counts.

    Returns:
        tuple[int, int]: minimum sum, starting index of the streak.
    """
    streak = 3
    n = len(steps)

    if n < streak:
        return None, None

    window_sum = sum(steps[:streak])
    min_sum = window_sum
    min_start = 0

    for i in range(streak, n):
        window_sum += steps[i] - steps[i-streak]
        if window_sum < min_sum:
            min_sum = window_sum
            min_start = i - streak + 1

    return min_sum, min_start


def longest_streak(steps, threshold=10000):
    """
    Find the longest streak (consecutive days) where each day’s steps ≥ threshold.

    Args:
        steps (list[int]): daily step counts.
        threshold (int): minimum steps per day to count towards streak.

    Returns:
        int: length of the longest streak.
    """
    n = len(steps)

    longest = 0
    start = 0

    for end in range(n):
        if steps[end] >= threshold:
            curr_win_size = end - start + 1
            longest = max(longest, curr_win_size)
        else:
            start = end + 1

    return longest


# Sample Data
daily_steps = [
    5234, 7890, 12034, 8765, 9345, 10234, 8456,
    10012, 11045, 7634, 5432, 9001, 11234, 10567,
    9800, 12345, 11000, 8700, 9500, 11890, 10400,
    9700, 8900, 10050, 11300, 9200, 8000, 10100,
    10750, 11500
]


# Results
max_sum, max_start = max_seven_day_streak(daily_steps)
print(f"📈 Maximum steps in any 7-day streak: {max_sum} (starting at day {max_start +1})")

min_sum, min_start = min_three_day_streak(daily_steps)
print(f"📉 Minimum steps in any 3-day streak: {min_sum} (starting at day {min_start +1})")

longest = longest_streak(daily_steps, threshold=10000)
print(f"🏆 Longest streak of days ≥ 10,000 steps: {longest} days")
