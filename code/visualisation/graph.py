from matplotlib import pyplot as plt
import pandas
import csv


def to_csv(solution_lengths, board_name):
    """ saves lengths of solutions and stores in a .csv file """

    # save a list of solution lengths as a csv file
    df = pandas.DataFrame(data={"solution lengths": solution_lengths})
    df.to_csv(f"data/output/Hillclimber_{board_name[:-4]}_{len(solution_lengths)}.csv", sep=',', index=False)


def histogram(csv_file_name, title=""):
    """ creates a histogram from a list of solution lengths """

    # read the csv into a list
    data = []

    with open(f"data/output/{csv_file_name}") as file:
        reader = csv.DictReader(file)

        for line in reader:
            data.append(int(line["solution lengths"]))

    # calculate the specs of the graph
    mean = round(sum(data) / len(data), 2)
    std = round((sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5, 2)
    lowest = min(data)
    highest = max(data)
    specs = f"Average: {mean}\nStandarddeviation: {std}\nLowest: {lowest}\nHighest: {highest}"

    # make a matplotlib histogram
    plt.hist(data, bins=int(len(data)/25), rwidth=0.9)
    plt.xlabel("Steps needed until solved")
    plt.ylabel("Count")
    x_values = list(range(10, max(data) + 10, 10))
    plt.xticks(x_values, rotation=40)
    plt.title(f"{title}, solved {len(data)} times with hillclimber")
    plt.grid(axis="y", alpha=0.75)

    # add the specs to the graph
    plt.text(x=highest-10, y=800, s=specs, horizontalalignment='center', fontstyle="italic")
    plt.gcf().subplots_adjust(bottom=0.2)
    plt.savefig(f"data/output/{csv_file_name[:-4]}.png")
    plt.close()


if __name__ == "__main__":
    histogram("Hillclimber_puzzle_1.csv", "Puzzle 1")
