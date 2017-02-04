#!/bin/python
from movielens import *
import numpy as np
from sklearn.metrics import mean_squared_error
import scipy.stats
# Store data in arrays
user = []
item = []
rating = []
rating_test = []

# Load the movie lens dataset into arrays
d = Dataset()
d.load_users("data/u.user", user)
d.load_items("data/u.item", item)
d.load_ratings("data/u.base", rating)
d.load_ratings("data/u.test", rating_test)
n = 150
n_users = len(user)
n_items = len(item)

# The utility matrix stores the rating for each user-item pair in the matrix form.
# Note that the movielens data is indexed starting from 1 (instead of 0).
utility = np.zeros((n_users, n_items))
for r in rating:
    utility[r.user_id-1][r.item_id-1] = r.rating
test = np.zeros((n_users, n_items))
for r in rating_test:
    test[r.user_id - 1][r.item_id - 1] = r.rating
# Finds the average rating for each user and stores it in the user's object
for i in range(n_users):
    rated = np.nonzero(utility[i])
    n = len(rated[0])
    if n != 0:
        user[i].avg_r = np.mean(utility[i][rated])
    else:
        user[i].avg_r = 0.



# Finds the Pearson Correlation Similarity Measure between two users
def pcs(x, y):
    """
    Insert your code here.
    """
    if x >=1 and y >= 1:
        x = clusteredutility[x-1]
        y = clusteredutility[y-1]
        return scipy.stats.pearsonr(x,y)[0]
    else:
        return 0.0

# Guesses the ratings that user with id, user_id, might give to item with id, i_id.
# We will consider the top_n similar users to do this.
def guess(rankingOfCorrelatedUser, user_id, i_id, top_n):
    """
    Insert your code here.
    """
    i = 1  # because we dont want to include user itself
    total = 0
    numberOfuserCounted= 0

    while (i <= top_n and i < n_users ):
        MostCorrelatedUserid = rankingOfCorrelatedUser[i]    # the most correlated user except itself  -1
        ratingOfithcorrelateduser = utility[MostCorrelatedUserid][i_id-1]
        ratingAfterScale = ratingOfithcorrelateduser - user[MostCorrelatedUserid].avg_r
        if ratingOfithcorrelateduser != 0:
            total += ratingAfterScale
            numberOfuserCounted +=1
        else:
            top_n += 1   #by increasing the limit we do another loop.
        i+=1

    if numberOfuserCounted==0:
        return user[user_id-1].avg_r  #should be average rating of this person
    else:
        return user[user_id-1].avg_r +total/numberOfuserCounted

clusteredutility = np.zeros((n_users,19))
for j in range(n_users):
    times = [0]*19
    for i in range(n_items):  # for each individual items
    #    print item[i].unknown == 1,utility[0][i]   #user 1 (0) #cluster 1 (0)
        if item[i].unknown == 1 and utility[j][i]!=0 :  # if it is unknown the 1st column in clustered utility
            clusteredutility[j][0] += utility[j][i]
            times[0] += 1 # couting how many of unknows are added
        if item[i].action == 1 and utility[j][i]!=0 :  # if it is action the 2nd column in clustered utility
            clusteredutility[j][1] += utility[j][i]
            times[1] += 1 # couting how many of unknows are added
        if item[i].adventure == 1 and utility[j][i]!=0 :  # if it is unknown the first column in clustered utility
            clusteredutility[j][2] += utility[j][i]
            times[2] += 1 # couting how many of unknows are added
        if item[i].animation == 1  and utility[j][i]!=0:  # if it is unknown the first column in clustered utility
            clusteredutility[j][3] += utility[j][i]
            times[3] += 1 # couting how many of unknows are added
        if item[i].childrens == 1  and utility[j][i]!=0:  # if it is unknown the first column in clustered utility
            clusteredutility[j][4] += utility[j][i]
            times[4] += 1 # couting how many of unknows are added
        if item[i].comedy == 1  and utility[j][i]!=0:  # if it is unknown the first column in clustered utility
            clusteredutility[j][5] += utility[j][i]
            times[5] += 1 # couting how many of unknows are added
        if item[i].crime == 1  and utility[j][i]!=0:  # if it is unknown the first column in clustered utility
            clusteredutility[j][6] += utility[j][i]
            times[6] += 1 # couting how many of unknows are added
        if item[i].documentary == 1 and utility[j][i]!=0:  # if it is unknown the first column in clustered utility
            clusteredutility[j][7] += utility[j][i]
            times[7] += 1 # couting how many of unknows are added
        if item[i].drama == 1 and utility[j][i]!=0:  # if it is unknown the first column in clustered utility
            clusteredutility[j][8] += utility[j][i]
            times[8] += 1 # couting how many of unknows are added
        if item[i].fantasy == 1 and utility[j][i]!=0 :  # if it is unknown the first column in clustered utility
            clusteredutility[j][9] += utility[j][i]
            times[9] += 1 # couting how many of unknows are added
        if item[i].film_noir == 1 and utility[j][i]!=0 :  # if it is unknown the first column in clustered utility
            clusteredutility[j][10] += utility[j][i]
            times[10] += 1 # couting how many of unknows are added
        if item[i].horror == 1 and utility[j][i]!=0:  # if it is unknown the first column in clustered utility
            clusteredutility[j][11] += utility[j][i]
            times[11] += 1 # couting how many of unknows are added
        if item[i].musical == 1 and utility[j][i]!=0:  # if it is unknown the first column in clustered utility
            clusteredutility[j][12] += utility[j][i]
            times[12] += 1 # couting how many of unknows are added
        if item[i].mystery == 1 and utility[j][i]!=0:  # if it is unknown the first column in clustered utility
            clusteredutility[j][13] += utility[j][i]
            times[13] += 1 # couting how many of unknows are added
        if item[i].romance == 1 and utility[j][i]!=0 :  # if it is unknown the first column in clustered utility
            clusteredutility[j][14] += utility[j][i]
            times[14] += 1 # couting how many of unknows are added
        if item[i].sci_fi == 1 and utility[j][i]!=0 :  # if it is unknown the first column in clustered utility
            clusteredutility[j][15] += utility[j][i]
            times[15] += 1 # couting how many of unknows are added
        if item[i].thriller == 1 and utility[j][i]!=0 :  # if it is unknown the first column in clustered utility
            clusteredutility[j][16] += utility[j][i]
            times[16] += 1 # couting how many of unknows are added
        if item[i].war == 1 and utility[j][i]!=0 :  # if it is unknown the first column in clustered utility
            clusteredutility[j][17] += utility[j][i]
            times[17] += 1 # couting how many of unknows are added
        if item[i].western == 1 and utility[j][i]!=0 :  # if it is unknown the first column in clustered utility
            clusteredutility[j][18] += utility[j][i]
            times[18] += 1 # couting how many of unknows are added
    for k in range(19):
         if times[k]!=0:
            clusteredutility[j][k] =clusteredutility[j][k]/ times[k]
utility_copy = np.copy(utility)
for i in range(n_users):
    coef = [0] * n_users
    for num in range(n_users):
        coef [num] = pcs(i+1,num+1)
    rankingOfCorrelatedUser = [idx[0] for idx in sorted(enumerate(coef), key=lambda x:x[1],reverse=True)] # from 1 to -1 sorting index
    for j in range(n_items):
        if utility_copy[i][j] == 0:
            utility_copy[i][j] = guess(rankingOfCorrelatedUser, i+1, j+1, n)
## THINGS THAT YOU WILL NEED TO DO:
# Perform clustering on users and items
# Predict the ratings of the user-item pairs in rating_test
# Find mean-squared error

y_true = []
y_pred = []
f = open('test.txt', 'w')
for i in range(0, n_users):
    for j in range(0, n_items):
        if test[i][j] > 0:     
            f.write("%d, %d, %d\n" % (i+1, j+1, utility_copy[i][j]))
            y_true.append(test[i][j])
            y_pred.append(utility_copy[i][j])
f.close()

print "Mean Squared Error: %f" % mean_squared_error(y_true, y_pred)
