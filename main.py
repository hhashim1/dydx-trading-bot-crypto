from constants import ABORT_ALL_POSITIONS, FIND_COINTEGRATED, PLACE_TRADERS, MANAGE_EXITS
from func_connections import connect_dydx
from func_private import abort_all_positions
from func_public import construct_market_prices
from func_cointegration import store_cointegration_results
from func_entry_pairs import open_positions
from func_exit_pairs import manage_trade_exits
from func_messaging import send_message

if __name__ == "__main__":
    
    send_message("anoter awesome message")
    print("success")
    exit(1)

    # Connect to client
    try:
        print("Connecting to Client...")
        client = connect_dydx()
    except Exception as e:
        print(e)
        print("Error connecting to client: ", e)
        exit(1)

    if ABORT_ALL_POSITIONS:
        try:
            print("Closing all positions")
            close_orders = abort_all_positions(client)
        except Exception as e:
            print("Error closing all positions", e)
            exit(1)


    # Find Cointegrated Pairs
    if FIND_COINTEGRATED:
        # Construct Market Prices
        try:
            print("Fetching market prices, please allow 3 mins...")
            df_market_prices = construct_market_prices(client)
        except Exception as e:
            print("Error constructing market prices: ", e)
            exit(1)

            
        # Store Cointegrated Pairs
        try:
            print("Storing cointegrated pairs...")
            stores_result = store_cointegration_results(df_market_prices)
            if stores_result != "saved":
                print("Error saving cointegrated pairs")
                exit(1)
        except Exception as e:
            print("Error saving cointegrated pairs: ", e)
            exit(1)

    # Run as always on
    while True:            
    
        # Place traders for opening positions
        if MANAGE_EXITS:
            try:
                print("Managing exits...")
                manage_trade_exits(client)
            except Exception as e:
                print("Error managing exiting positions: ", e)
                exit(1)                
    

        # Place traders for opening positions
        if PLACE_TRADERS:
            try:
                print("Finding trading opportunities...")
                open_positions(client)
            except Exception as e:
                print("Error trading pairs: ", e)
                exit(1)                