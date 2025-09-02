def execute_transaction(client, asset, quantity, action):
    if action == "buy":
        client.portfolio[asset] = client.portfolio.get(asset, 0) + quantity
    elif action == "sell":
        if client.portfolio.get(asset, 0) >= quantity:
            client.portfolio[asset] -= quantity
        else:
            print("Insufficient holdings to sell.")
    else:
        print("Invalid transaction type.")
