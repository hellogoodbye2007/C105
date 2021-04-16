import csv
with open('class1.csv', newline= '') as f:

reader = csv.reader(f)
fine_data = list(reader)
# To remover header from csv
file_data.pop(0)
total_marks = 0
total_entries = len(file_data)

for marks in file_data:
    total_marks += float(marks)

mean = total_marks/total_entries
print(f"The mean is {mean}")
import pandas as pd
import plotly.express as px
df = pd.read_csv("class1.csv")
fig = px.scatter(df, x = "student number", y = "marks")
fig.update_layout(shapes = [
    dict(
        type = 'line',
        y0 = mean, y1 = mean,
        x0 = 0, x1 = total_entries,
    )
])

fig.update_yaxis(rangemode = "tozero")
fig.show()

sumOfDistances = 0
for marks in file_data:
    sumOfSquares += float((mean-marks)^2)

standardDeviationSquared = sumOfSquares/total_entries
standardDeviation = sqrt(standardDeviationSquared)
