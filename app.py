# Create dictionary(poll) to store Candidates & Vote count starting at 0

poll = {
    "APC": {
        "Karen Joy": 0,
    },
    "PDP": {
        "": 0,
    },
    "APGA": {
        "Ben White": 0,
    },
    "AD": {
        "John Doe": 0,
    },
    "LP": {
        "Peter Obi": 0,
    }
}

# get registered voters
getRegisteredVoters = int(input("Enter number of registered voters"))

# Display Party to voters
parties = poll.keys()
print("Vote a running party\n")
for party in parties:
    print(party)

# Get vote choice from voters
vote = input("Choose your party: ")

