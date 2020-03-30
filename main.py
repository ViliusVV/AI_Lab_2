import numpy
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sun_data = pd.read_csv("data/sunspot.txt", sep='\t')


if __name__ == "__main__":
    print(sun_data)

    sun_data.plot(style="-", x="Metai")
    plt.title("Saulės dėmių aktyvumo (1700-2014) grafikas")
    plt.ylabel("Dėmės")
    plt.show()

    L = sun_data.shape[0]
    P = [ sun_data.Dėmės[0:L - 1], sun_data.Dėmės[1:L] ]
    print(P)

