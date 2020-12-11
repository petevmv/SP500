file_handle = open("SP500.txt")
lines = file_handle.readlines()
SPclose = []
interest = []
for line in lines[6:18]:
    SPclose.append(float(line.split(',')[1]))
    interest.append(float(line.split(',')[5]))
mean_SP = sum(SPclose)/len(SPclose)
max_interest = max(interest)
