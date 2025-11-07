#Implement job sequencing with deadlines using a greedy method. (DAA)

# ---------- Job Sequencing with Deadlines using Greedy Method ----------

class Job:
    def __init__(self, job_id, profit, deadline):
        self.job_id = job_id
        self.profit = profit
        self.deadline = deadline

def job_sequencing(jobs, n):
    # Step 1: Sort jobs by decreasing profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Step 2: Find maximum deadline
    max_deadline = max(job.deadline for job in jobs)

    # Step 3: Initialize slots (-1 means empty)
    slots = [-1] * (max_deadline + 1)

    total_profit = 0
    sequence = []

    # Step 4: Assign jobs to slots
    for job in jobs:
        for d in range(job.deadline, 0, -1):  # check available slot before deadline
            if slots[d] == -1:
                slots[d] = job.job_id
                total_profit += job.profit
                sequence.append(job.job_id)
                break

    return sequence, total_profit

# ---------- Main Function ----------
if __name__ == "__main__":
    print("----- Job Sequencing with Deadlines -----")
    n = int(input("Enter number of jobs: "))
    jobs = []

    for i in range(n):
        job_id = input(f"Enter Job ID {i+1}: ")
        profit = int(input(f"Enter Profit for {job_id}: "))
        deadline = int(input(f"Enter Deadline for {job_id}: "))
        jobs.append(Job(job_id, profit, deadline))

    sequence, total_profit = job_sequencing(jobs, n)

    print("\nOptimal Job Sequence:", sequence)
    print("Total Profit:", total_profit)
