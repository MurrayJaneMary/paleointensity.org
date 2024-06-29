
exp="MMSS13-1A"
lamda = 0.20
theta = 172
customT = 65


# Format lamda to appear as 020
lamda_formatted = f"{lamda:.2f}".replace('.', '')

modelFile = f'modres_customT{customT}_lambda{lamda_formatted}_theta{theta}.th'
print(modelFile)
