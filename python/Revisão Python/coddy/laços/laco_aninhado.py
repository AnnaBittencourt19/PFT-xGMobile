# Get input for rows and columns
rows = int(input())
cols = int(input())

for row in range(rows):
    line = "" #Pula linha
    for col in range(cols):
        line += "*" # As colunas são *
    print(line) 
