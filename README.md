# BinanceAutoSellToUSDT

BinanceAutoSell is a Python tool designed for Binance users who wish to quickly liquidate their crypto assets into USDT. 
This script leverages the Binance API to analyze your portfolio, adjust selling quantities based on Binance's minimum trade requirements, and execute market sells for each asset into USDT.

## Features
- Automatic selling of all crypto assets into USDT
- Automatic calculation of selling quantities based on Binance's requirements
- Efficient API exception handling

## Prerequisites
- Binance account with API Key and Secret Key
- Python 3.x
- `binance-python` package

## Installation
1. Clone this repository: `git clone https://github.com/DavideFranchioni/BinanceAutoSellToUSDT.git`
2. Install dependencies: `pip install -r requirements.txt`

## Configuration
Insert your Binance API Key and Secret Key in `main.py`:
api_key = 'your-api-key'
api_secret = 'your-secret-key'
