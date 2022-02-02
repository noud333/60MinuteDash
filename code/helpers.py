import pandas


def save(solution, filename):
    """ save the solution as a csv file  """

    df = pandas.DataFrame(data={"car": solution[0], "move": solution[1]})
    df.to_csv(f"data/output/{filename}", sep=',', index=False)
