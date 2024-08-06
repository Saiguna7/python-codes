# Initialize the price range from Rs 0.50 to Rs 5.00 with increments of Rs 0.50
price_range = [0.50, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50, 5.00]

# Initialize the bids from different players for each price
bids = {
    'Player 1': [25, 25, 25, 25, 50, 50, 50, 50, 50, 50],
    'Player 2': [25, 25, 25, 25, 50, 50, 50, 50, 50, 50],
    'Player 3': [50, 50, 50, 50, 50, 50, 50, 50, 50, 100],
    'Player 4': [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
    'Player 5': [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
}

# Calculate the total supply and demand at each price
total_supply = [sum(bids[player][i] for player in bids) for i in range(len(price_range))]
total_demand = [0] * len(price_range)

# Initialize the market clearing price and volume
market_clearing_price = None
market_clearing_volume = 0

# Determine the market clearing price and volume
for i in range(len(price_range)):
    total_demand[i] = sum(bids[player][i] for player in bids)
    if total_supply[i] >= total_demand[i]:
        market_clearing_price = price_range[i]
        market_clearing_volume = total_demand[i]
        break

# Display the supply curve
print("Supply Curve:")
for i in range(len(price_range)):
    print(f"Price: Rs {price_range[i]:.2f}, Total Supply: {total_supply[i]}")

# Display the demand curve
print("\nDemand Curve:")
for i in range(len(price_range)):
    print(f"Price: Rs {price_range[i]:.2f}, Total Demand: {total_demand[i]}")

# Display the market clearing price and volume
print(f"\nMarket Clearing Price: Rs {market_clearing_price:.2f}")
print(f"Market Clearing Volume: {market_clearing_volume}")

# Participants who have been shortlisted
shortlisted_players = [player for player in bids if sum(bids[player]) > market_clearing_volume]
print("\nParticipants who have been shortlisted:")
for player in shortlisted_players:
    print(player)
