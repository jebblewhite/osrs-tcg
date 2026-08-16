TOTAL_CARDS = 6376

RARITY_THRESHOLDS = [
    ("GODLY",      0.98),
    ("MYTHIC",     0.95),
    ("LEGENDARY",  0.90),
    ("EPIC",       0.75),
    ("RARE",       0.50),
    ("UNCOMMON",   0.25),
    ("COMMON",     0.00),
]

card_pool = {}

for card_id in range(1, TOTAL_CARDS + 1):

    percentile = card_id / TOTAL_CARDS

    for rarity, threshold in RARITY_THRESHOLDS:
        if percentile >= threshold:
            card_pool[card_id] = rarity
            break



from collections import defaultdict

cards_by_rarity = defaultdict(list)

for card_id, rarity in card_pool.items():
    cards_by_rarity[rarity].append(card_id)

RARITIES = [
    "COMMON",
    "UNCOMMON",
    "RARE",
    "EPIC",
    "LEGENDARY",
    "MYTHIC",
    "GODLY"
]

WEIGHTS = [
    37.34,
    32.00,
    16.00,
    8.00,
    4.00,
    2.00,
    0.66
]

import random

def generate_card():

    rarity = random.choices(
        RARITIES,
        weights=WEIGHTS,
        k=1
    )[0]

    return random.choice(cards_by_rarity[rarity])

def generate_pack(size=5):

    pack = []

    while len(pack) < size:

        card = generate_card()

        if card not in pack:
            pack.append(card)

    return pack


def simulate_collection():

    collection = set()
    packs_opened = 0

    while 1 not in collection:

        packs_opened += 1

        pack = generate_pack()
        collection.update(pack)

        collection_size = len(collection)


    return packs_opened

import pandas as pd

def monte_carlo(n_simulations=10000):

    results = []

    for _ in range(n_simulations):
        results.append(simulate_collection())

    return pd.DataFrame(results)

df = monte_carlo()

df.to_json('monte_carlo_coins_10000.json')

print(df.mean())
print(df.median())
print(df.std())
print(df.quantile([0.05, 0.50, 0.95]))