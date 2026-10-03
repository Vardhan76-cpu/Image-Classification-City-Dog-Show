def print_results(
        results_dic,
        results_stats,
        model,
        print_incorrect_dogs=False,
        print_incorrect_breed=False):

    print(
        "\n\n*** Results Summary for CNN Model Architecture",
        model.upper(),
        "***"
    )

    print(
        "{:20}: {:3d}".format(
            "N Images",
            results_stats["n_images"]
        )
    )

    print(
        "{:20}: {:3d}".format(
            "N Dog Images",
            results_stats["n_dogs_img"]
        )
    )

    print(
        "{:20}: {:3d}".format(
            "N Not-Dog Images",
            results_stats["n_notdogs_img"]
        )
    )

    print(
        "\n{:20}: {:5.1f}%".format(
            "pct_match",
            results_stats["pct_correct"]
        )
    )

    print(
        "{:20}: {:5.1f}%".format(
            "pct_correct_dogs",
            results_stats["pct_correct_dogs"]
        )
    )

    print(
        "{:20}: {:5.1f}%".format(
            "pct_correct_breed",
            results_stats["pct_correct_breed"]
        )
    )

    print(
        "{:20}: {:5.1f}%".format(
            "pct_correct_notdogs",
            results_stats["pct_correct_notdogs"]
        )
    )

    if print_incorrect_dogs:

        print("\n*** Incorrect Dog Classifications:")

        for key in results_dic:

            if (
                results_dic[key][3] == 1
                and
                results_dic[key][4] == 0
            ):

                print(
                    "Real Dog:",
                    results_dic[key][0],
                    "Classifier:",
                    results_dic[key][1],
                    "File:",
                    key
                )

    if print_incorrect_breed:

        print("\n*** Incorrect Dog Breed Classifications:")

        for key in results_dic:

            if (
                results_dic[key][3] == 1
                and
                results_dic[key][4] == 1
                and
                results_dic[key][2] == 0
            ):

                print(
                    "Real Dog:",
                    results_dic[key][0],
                    "Classifier:",
                    results_dic[key][1],
                    "File:",
                    key
                )