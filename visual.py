import database
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
This module is responsible for visualising the data retrieved from a database using Matplotlib.
"""

"""
Task 28 - 30: Write suitable functions to visualise the data as follows:

- Display the top 5 countries for confirmed cases using a pie chart
- Display the top 5 countries for death for specific dates using a bar chart
- Display a suitable (animated) visualisation to show how the number of confirmed cases, deaths and recovery change over
time. This could focus on a specific country/countries.

Each function for the above should utilise the functions in the module 'database' to retrieve any data.
You may add additional methods to the module 'database' if needed. Each function should then visualise
the data using Matplotlib.
"""


# 28
# Display the top 5 countries for confirmed cases using a pie chart
def display_top5_with_pie():
    confirmed_size = []
    countries = []
    data = database.retrieve_top5()
    for record in data:
        countries.append(record[0])
        confirmed_size.append(record[1])

    my_colors = ("yellow", "red", "green", "purple", "blue")
    plt.pie(confirmed_size, labels=countries, autopct='%1.1f%%', shadow=True, colors=my_colors, startangle=30)
    plt.title("TOP FIVE COUNTRIES FOR CONFIRMED CASES")
    plt.axis("equal")
    plt.show()


# 29 Display the top 5 countries for death for specific dates using a bar chart

def display_top5_c_with_bar():
    countries = []
    death_records = []
    info_death = database.retrieve_top5_det()
    for record in info_death:
        countries.append(record[8])
        death_records.append(record[4])

    my_color = "green"
    plt.bar(countries, height=death_records, width=0.4, color=my_color)
    plt.title("TOP FIVE COUNTRIES FOR DEATH COUNTS")
    plt.xlabel("COUNTRIES")
    plt.ylabel("DEATH COUNTS")
    plt.show()


# 30
# Display a suitable (animated) visualisation to show how the number of confirmed cases, deaths and recovery change over
# time. This could focus on a specific country/countries.

fig, ax = plt.subplots()  # for mainland china only


def animated(frame):
    obs_date = []
    confirmed = []
    death = []
    recovered = []
    feeds = database.retrieve_country_info_an()
    for record in feeds:
        obs_date.append(record[0])
        confirmed.append(record[2])
        death.append(record[3])
        recovered.append(record[4])

    global ax

    ax.set_xlim(0, 9)
    ax.set_xlabel("OBSERVATION  DATES")
    ax.set_ylim(0, 5810)
    ax.set_ylabel("COUNTS")
    ax.plot(obs_date, confirmed, "ro")
    ax.plot(obs_date, death, "ys")
    ax.plot(obs_date, recovered, "g^")
    plt.title("CHANGES IN RECORD OVER TIME (Mainland China (Jan,2020))")
    ax.legend(labels=["confirmed cases", "death cases", "recovery cases"],
              loc="upper left")


def run():
    global fig
    my_animation = animation.FuncAnimation(fig, animated, frames=10,
                                           interval=1000)
    plt.show()

display_top5_with_pie()