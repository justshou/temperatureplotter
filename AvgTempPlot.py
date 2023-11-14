import matplotlib.pyplot as plt

def main():
    avghigh = []
    city = input("Enter city: ")
    year = input("Enter year: ")
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    print(avghigh)
    avghigh = input("Enter average high temperature for each month of the year: ").split(" ")
    for nums in range(len(avghigh)):
        avghigh[nums] = int(avghigh[nums])
    
    # plots the chart
    plt.plot(months, avghigh, marker='o')
    
    #labels and grid
    plt.title(f'{year} Average Monthly High Temperature - {city}')
    plt.xlabel(f'Months')
    plt.ylabel(f'Temperature')
    plt.grid(True)

    #limits
    plt.xlim(xmin=0, xmax=12)
    plt.ylim(ymin=0, ymax=100)

    # show chart
    plt.show()
main()