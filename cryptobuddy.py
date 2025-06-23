# 🤖 CryptoBuddy - AI-Powered Crypto Advisor Chatbot

# Sample Crypto Dataset
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

# Chatbot logic
def get_recommendation(query):
    query = query.lower()

    if "sustainable" in query or "eco" in query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"🌱 I recommend {recommend}! It's eco-friendly and has long-term potential."

    elif "trending" in query or "profitable" in query:
        best = []
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                best.append(coin)
        if best:
            return f"🚀 {', '.join(best)} is/are trending and look profitable!"
        else:
            return "📉 No highly trending cryptos at the moment. Try again later."

    elif "long-term" in query or "growth" in query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                return f"📈 {coin} is rising and has strong sustainability — great for long-term growth!"

    elif "cardano" in query or "bitcoin" in query or "ethereum" in query:
        coin = query.title()
        if coin in crypto_db:
            data = crypto_db[coin]
            return (
                f"{coin} info:\n"
                f"📊 Price Trend: {data['price_trend']}\n"
                f"💰 Market Cap: {data['market_cap']}\n"
                f"⚡ Energy Use: {data['energy_use']}\n"
                f"🌍 Sustainability Score: {data['sustainability_score'] * 10}/10"
            )

    return "🤖 Sorry, I didn’t understand that. Try asking about 'trending', 'sustainable', or 'long-term' cryptos."
  
  # Run this cell every time you want to ask the bot something
user_query = input("Ask CryptoBuddy a question: ")
response = get_recommendation(user_query)
print("CryptoBuddy:", response)
