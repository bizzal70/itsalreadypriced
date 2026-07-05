FEEDS = [
    # Incident / exploit trackers (highest signal for the security spine)
    {"name": "Rekt News", "url": "https://rekt.news/rss/", "category": "incident"},
    {"name": "Chainalysis Blog", "url": "https://www.chainalysis.com/blog/feed/", "category": "research"},

    # Crypto news + markets
    {"name": "CoinDesk", "url": "https://www.coindesk.com/arc/outboundfeeds/rss/", "category": "news"},
    {"name": "Cointelegraph", "url": "https://cointelegraph.com/rss", "category": "news"},
    {"name": "Decrypt", "url": "https://decrypt.co/feed", "category": "news"},
    {"name": "Bitcoin Magazine", "url": "https://bitcoinmagazine.com/feed", "category": "markets"},
    {"name": "The Defiant", "url": "https://thedefiant.io/api/feed", "category": "defi"},

    # General security press that reliably covers crypto thefts, drainers, DPRK ops
    {"name": "The Hacker News", "url": "https://feeds.feedburner.com/TheHackersNews", "category": "security"},
    {"name": "Bleeping Computer", "url": "https://www.bleepingcomputer.com/feed/", "category": "security"},

    # Community signal (Reddit RSS, no API key needed)
    {"name": "r/CryptoCurrency", "url": "https://www.reddit.com/r/CryptoCurrency/.rss", "category": "news"},
    {"name": "r/defi", "url": "https://www.reddit.com/r/defi/.rss", "category": "defi"},
    {"name": "r/ethdev", "url": "https://www.reddit.com/r/ethdev/.rss", "category": "research"},
]
