import modules.polling as polling, modules.voting as voting

# get registered voters
getRegisteredVoters = int(input("Enter number of registered voters: "))

# count votes
vote_count = 0 #initialise vote_count variable to track votes
while vote_count < getRegisteredVoters:
    # call get_votes method from voting module and update count variable
    voting.get_votes()
    vote_count = vote_count + 1
