# main2:
# solve the board and show the solution
# greedy = Greedy(board)
# solution, random_solved_board = greedy.run()
# solution_length = len(solution[0])
# print(f"--- Solution: {solution_length} ---")

simulate_random = Simulate_random(board)
solution, solved_board = simulate_random.simulate_n(10)

# save the solution as a csv file with the name output
save(solution, filename="output.csv")

# show the result of the solution
print(f"--- Random solution:")
print(f"--- {len(solution[0])} steps ---")

# visualize the solution making use of pygame
visualize_csv(output="output.csv", original_board=board)

# main1:

    # # show the result of random solutions
    # print(f"--- Random solutions:")
    # steps = []
    # total_steps = 1000
    # for i in range(total_steps):

    #     # solve the board and show the solution
    #     solution, random_solved_board = random_solve(board)
    #     solution_length = len(solution[0])
    #     steps.append(solution_length)
    #     print(f"--- Solution{i}: {solution_length} ---")

    # # show the average number of steps 
    # print("--- Average steps: ", sum(steps) / len(steps))

    # # save steps to a csv file
    # with open(f"data/output/steps.csv", "w") as file:
    #     writer = csv.writer(file)
    #     writer.writerow(["Steps"])
    #     for step in steps:
    #         writer.writerow([step])


    with open(f"data/output/steps.csv", "r") as file:
        reader = csv.DictReader(file)
        steps = []
        for x in reader:
            steps.append(int(x["Steps"]))
    
    # calculate mean
    steps.sort()
    #steps = steps[25:975]
    total_steps = len(steps)

    avg = sum(steps) / len(steps)
    print("Average: ", avg)
    # calculate variance using a list comprehension
    var_res = sum((xi - avg) ** 2 for xi in steps) / len(steps)
    res = statistics.variance(steps)
    print("Variance: ", res)
    print("Variance: ", var_res)

    skew = (math.sqrt(total_steps) * sum((xi - avg) ** 3 for xi in steps)) / (sum((xi - avg) ** 2 for xi in steps)) ** (3 / 2)
    kurt = (total_steps * sum((xi - avg) ** 4 for xi in steps)) / (sum((xi - avg) ** 2 for xi in steps)) ** 2 - 3

    print("Skewness: ", skew)
    print("Kurtosis: ", kurt)


    plt.hist(steps, bins=100)
    plt.savefig("test.png")

    # save the solution as a csv file with the name output
    #save(solution, filename="output.csv")

    # show the result of the solution
    #print(f"--- Random solution:")
    #print(f"--- {len(solution[0])} steps ---")
    
    # visualize the solution making use of pygame
    #visualize_csv(output="output.csv", original_board=board)
