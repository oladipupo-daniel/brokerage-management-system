def display_portfolio(client):
    print(f"\nPortfolio for {client.name}:")
    if not client.portfolio:
        print("No assets yet.")
    for asset, qty in client.portfolio.items():
        print(f"{asset}: {qty}")
