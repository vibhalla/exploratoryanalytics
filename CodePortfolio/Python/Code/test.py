def main():
    print("Program to calculate assignment group averages.\n")
    import numpy as np
    scores = np.load("../Data/scores.npy")
    scores_only = scores[1:]
    feedList = ["Homework average:",1,6],["Lab average:",7,17],["Quiz average:",20,28],["Project average:",18,18],["Midterm 1 average:",19,19],["Midterm 2 average:",29,29]
    for i in range(len(feedList)):
        if feedList[i][1] == feedList[i][2]:
            outValue = np.around(scores_only[:,feedList[i][1]].sum(axis=0)/(scores_only.shape[0]), decimals = 1)
            print("feed",feedList[i][1],"score",scores_only.shape[0])
        else:
            outValue = np.around(scores_only[:,feedList[i][1]:feedList[i][2]+1].sum()/(scores_only.shape[0]*(feedList[i][2]-feedList[i][1]+1)), decimals = 1) 
            print("feed1",feedList[i][1],"score1",scores_only.shape[0])
            print(outValue)
        outString = '{:<18}'.format(feedList[i][0])+'{:>5}'.format(outValue)
        print(outString)
    # user input is requested to allow the runtime window to remain visible until the user decides to exit
    input("\nPress the Enter key to exit ")
main()