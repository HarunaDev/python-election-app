import modules.polling as polling

def get_votes():
    # Display Party to voters
    parties = polling.poll.keys()
    print("Vote a running party\n")
    for party in parties:
        print(party)

    # Get vote choice from voters
    vote = input("Choose your party: ")
    print("Thank you for voting")