# Taking user input
n = int(input("Enter the number of jobs: "))

profits = list(map(int, input("Enter profits separated by spaces: ").split()))
jobs = input("Enter job names separated by spaces: ").split()
deadlines = list(map(int, input("Enter deadlines separated by spaces: ").split()))

# Combine job details and sort by profit in descending order
profitNJobs = sorted(zip(profits, jobs, deadlines), key=lambda x: x[0], reverse=True)

# Find the maximum deadline to determine the number of slots
max_deadline = max(deadlines)
slot = [0] * (max_deadline + 1)  
ans = ['null'] * (max_deadline + 1)

total_profit = 0

for job in profitNJobs:
    for j in range(min(max_deadline, job[2]), 0, -1):
        if slot[j] == 0:
            ans[j] = job[1]
            total_profit += job[0]
            slot[j] = 1
            break

# Remove "null" entries for better display
scheduled_jobs = [job for job in ans[1:] if job != 'null']

print("Jobs scheduled:", scheduled_jobs)
print("Total profit:", total_profit)
