from binance.client import Client
from binance.exceptions import BinanceAPIException
from decimal import Decimal, ROUND_DOWN


# Sostituisci con le tue chiavi API
api_key = ''
api_secret = ''

client = Client(api_key, api_secret)


def adjust_quantity(symbol, quantity):
    info = client.get_symbol_info(symbol)
    for f in info['filters']:
        if f['filterType'] == 'LOT_SIZE':
            step_size = Decimal(f['stepSize'])
            min_qty = Decimal(f['minQty'])
            break

    # Calcola il numero di cifre decimali per lo step size
    step_size_scale = step_size.as_tuple().exponent

    # Arrotonda la quantità all'incremento di step size più vicino senza eccedere
    adjusted_qty = (Decimal(quantity) // step_size * step_size).quantize(Decimal(str(step_size)))

    print(
        f"Symbol: {symbol}, Step Size: {step_size}, Min Qty: {min_qty}, Original Qty: {quantity}, Adjusted Qty: {adjusted_qty}")

    # Controlla se la quantità adattata rispetta il minQty
    if adjusted_qty < min_qty:
        print(f"La quantità adattata {adjusted_qty} è inferiore al minimo richiesto {min_qty}")
        return Decimal('0')

    return adjusted_qty


try:
    account_info = client.get_account()
    balances = account_info['balances']

    for balance in balances:
        asset = balance['asset']
        free_balance = float(balance['free'])

        if asset != 'USDT' and free_balance > 0:
            symbol = asset + 'USDT'
            try:
                client.get_symbol_info(symbol)

                adjusted_qty = adjust_quantity(symbol, free_balance)

                if adjusted_qty > 0:
                    order = client.order_market_sell(symbol=symbol, quantity=str(adjusted_qty))
                    print(f"Ordine eseguito: Venduto {adjusted_qty} di {asset} in USDT", order)
                else:
                    print(f"Quantità di {asset} troppo bassa per essere venduta, inferiore a minQty.")
            except BinanceAPIException as e:
                print(f"Errore nella vendita di {asset}: {e}")
except BinanceAPIException as e:
    print(f"Errore API Binance: {e}")