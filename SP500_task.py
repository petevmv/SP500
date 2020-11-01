fileh = open("SP500.txt")
lines = fileh.readlines()

closing_idx_lst = []
intrest_rate = []
for row in lines[6:18]:
    vals = row.strip().split(',')
    closing_idx_lst.append(vals[1])
    intrest_rate.append(vals[5])

mean_SP = sum(map(float, closing_idx_lst))/len(closing_idx_lst)

print(mean_SP)

intrest_rate_float = []
for el in  intrest_rate:
    intrest_rate_float.append(float(el))

max_interest = 0
for f_el in intrest_rate_float:
        if f_el > max_interest:
            max_interest = f_el
print(max_interest)
