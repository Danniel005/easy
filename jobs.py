def job_scheduling(jobs):
    # Sort jobs in decreasing order of profit
    jobs.sort(key=lambda x: x[1], reverse=True)

    n = len(jobs)
    result = [False] * n
    slots = [False] * n

    for i in range(n):
        for j in range(min(n, jobs[i][0]) - 1, -1, -1):
            if not slots[j]:
                result[j] = jobs[i][2]
                slots[j] = True
                break

    return result

# Example usage
jobs = [
    (4, 20, 'a'),
    (1, 10, 'b'),
    (1, 40, 'c'),
    (1, 30, 'd')
]

schedule = job_scheduling(jobs)
print("Following is the maximum profit sequence of jobs:", schedule)
