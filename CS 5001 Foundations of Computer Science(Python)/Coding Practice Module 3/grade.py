"""
    Hang Zhao
    9/18/2023
    receives a score and returns the letter
    grade for that score.
"""
# receives a score and returns
# the letter grade for that score.


def grade(score):
    if score > 92:
        return 'A'
    elif score >= 90 and score <= 92:
        return 'A-'
    elif score >= 86 and score <= 89:
        return 'B+'
    elif score >= 82 and score < 86:
        return 'B'
    elif score >= 77 and score <= 81:
        return 'B-'
    elif score > 72 and score < 77:
        return 'C+'
    elif score > 68 and score <= 72:
        return 'C'
    elif score >= 65 and score <= 68:
        return 'C-'
    else:
        return 'F'


def main():
    score = int(input())
    print(grade(score))


if __name__ == "__main__":
    main()
