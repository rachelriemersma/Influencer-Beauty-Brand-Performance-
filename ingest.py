print("script started")
import pandas as pd
from sqlalchemy import create_engine
import os

# Create database
engine = create_engine('sqlite:///beauty_trends.db')

# Influencer Brand Classification
influencer_brands = [
    'rare beauty by selena gomez',
    'fenty beauty by rihanna',
    'fenty skin',
    'summer fridays',
    'one/size by patrick starrr',
    'refy',
    'danessa myricks beauty',
    'haus labs by lady gaga',
    'pattern by tracee ellis ross',
    'lawless',
    'makeup by mario',
    'gxve by gwen stefani',
    'jlo beauty',
    'kora organics',
    'pat mcgrath labs',
    'patrick ta',
    'jvn',
    'gisou',
    'forvr mood',
    'wishful',
    'nudestix',
    'dominique cosmetics',
    'one/size by patrick starrr',
    'cay skin',
    'huda beauty',
]
# Prestige Brand Classification
prestige_brands = [
    'la mer',
    'augustinus bader',
    'dr. barbara sturm',
    'tatcha',
    'sisley',
    'sk-ii',
    'sulwhasoo',
    'chanel',
    'dior',
    'tom ford',
    'hermès',
    'kilian paris',
    'armani beauty',
    'yves saint laurent',
    'guerlain',
    'givenchy',
    'valentino',
    'prada',
    'gucci',
    'viktor&rolf',
    'maison margiela',
    'acqua di parma',
    'jo malone london',
    'charlotte tilbury',
    'westman atelier',
    'pat mcgrath labs',
    'natasha denona',
    'laura mercier',
    'bobbi brown',
    'estée lauder',
    'lancôme',
    'shiseido',
    'kérastase',
    'oribe',
    'christophe robin',
    'rossano ferretti parma',
]

def classify_brand(brand_name):
    b = str(brand_name).lower()
    if b in influencer_brands:
        return 'influencer'
    elif b in prestige_brands:
        return 'prestige'
    else:
        return 'traditional'

# --- LOAD PRODUCTS ---
print("Loading products...")
products = pd.read_csv('data/product_info.csv')
products = products[[
    'product_id', 'product_name', 'brand_name', 'rating',
    'reviews', 'loves_count', 'price_usd', 'primary_category',
    'secondary_category', 'limited_edition', 'new', 'sephora_exclusive'
]]
products['brand_type'] = products['brand_name'].apply(classify_brand)
products.to_sql('products', engine, if_exists='replace', index=False)
print(f"  Loaded {len(products)} products")

# --- LOAD REVIEWS ---
review_files = [
    'data/reviews_0-250.csv',
    'data/reviews_250-500.csv',
    'data/reviews_500-750.csv',
    'data/reviews_750-1250.csv',
    'data/reviews_1250-end.csv'
]

print("Loading reviews...")
first = True
total = 0
for f in review_files:
    print(f"  Reading {f}...")
    df = pd.read_csv(f, usecols=[
        'author_id', 'rating', 'is_recommended', 'submission_time',
        'review_text', 'skin_tone', 'skin_type', 'product_id',
        'brand_name', 'price_usd'
    ])
    df.to_sql('reviews', engine, if_exists='append' if not first else 'replace', index=False)
    total += len(df)
    first = False
    print(f"    {len(df)} rows loaded")

print(f"  Total reviews loaded: {total}")
print("\nDone! Database ready at beauty_trends.db")
