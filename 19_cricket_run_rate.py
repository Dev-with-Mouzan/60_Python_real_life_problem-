# Problem 19: Cricket Run Rate
# Runs scored in each over of a 20 over match are given as a list. Print total runs, run rate and the best over (over number and runs).
# Input [6,8,10,4,12,...]
# Output Total, Run Rate, Best Over

run_rate=[34,5,2,2,3,4,5,6,7,8,9,10,34,5,2,2,3,4,5,6,7,8,9,10]

print("total run: ",sum(run_rate))
print("average run rate: ",round(sum(run_rate)/len(run_rate),2))
print("highest run rate: ",max(run_rate))
