import pandas as pd

# list of all product families used in training
FAMILIES = [
"BABY CARE","BEAUTY","BEVERAGES","BOOKS","BREAD/BAKERY","CELEBRATION",
"CLEANING","DAIRY","DELI","EGGS","FROZEN FOODS","GROCERY I","GROCERY II",
"HARDWARE","HOME AND KITCHEN I","HOME AND KITCHEN II","HOME APPLIANCES",
"HOME CARE","LADIESWEAR","LAWN AND GARDEN","LINGERIE","LIQUOR,WINE,BEER",
"MAGAZINES","MEATS","PERSONAL CARE","PET SUPPLIES","PLAYERS AND ELECTRONICS",
"POULTRY","PREPARED FOODS","PRODUCE","SCHOOL AND OFFICE SUPPLIES","SEAFOOD"
]

def create_features(store, family, promotion):

    data = {
        "id":0,
        "store_nbr":store,
        "onpromotion":promotion,
        "day_of_week":3,
        "month":6,
        "year":2017,
        "week_of_year":25,
        "lag_7":200,
        "lag_14":210,
        "lag_28":220,
        "rolling_mean_7":205,
        "promo_lag_7":promotion
    }

    # create dataframe
    df = pd.DataFrame([data])

    # add family dummy columns
    for f in FAMILIES:
        col = f"family_{f}"
        df[col] = 1 if f == family else 0

    return df