from fastapi import FastAPI, Query
import random
import uvicorn

app = FastAPI()

side_hustles = [
    "Freelancing - Start offering your skills online!",
    "Dropshipping - Sell without handling inventory!",
    "Stock Market - Invest and watch your money grow!",
    "Affiliate Marketing - Earn by promoting products!",
    "Crypto Trading - Buy and sell digital assets!",
]

money_quotes = [
    "The way to get started is to quit talking and begin doing. – Walt Disney",
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn",
]

@app.get("/side_hustle")
def get_side_hustle(api_key: str = Query(None)):
    """Return a random side hustle idea"""
    # if api_key != "1234567890":
    #     return {"error": "Invalid API key"}
    return {"side_hustle": random.choice(side_hustles)}

@app.get("/money_quote")
def get_money_quote(api_key: str = Query(None)):
    """Return a random money quote"""
    # if api_key != "1234567890":
    #     return {"error": "Invalid API key"}
    return {"money_quote": random.choice(money_quotes)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
