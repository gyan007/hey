import matplotlib.pyplot as plt

# Data
gases = ['Nitrogen', 'Oxygen', 'Carbon Dioxide', 'Others']
percentages = [78, 21, 0.04, 0.96]  # approximate composition of air

# Create pie chart
plt.pie(
    percentages, 
    labels=gases, 
    autopct='%1.2f%%',  # show values as percentages
    startangle=90,      # rotate chart for better layout
    shadow=True         # add shadow for depth
)

# colors = ['skyblue', 'lightgreen', 'lightcoral', 'gold']
# plt.pie(percentages, labels=gases, autopct='%1.1f%%', colors=colors, startangle=140, explode=[0, 0, 0.1, 0])


plt.title("Composition of Air")
plt.show()
