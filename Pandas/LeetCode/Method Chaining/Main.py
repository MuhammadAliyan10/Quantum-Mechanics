import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    filterAnimals = animals[animals['weight'] > 100]
    sortedAnimals = filterAnimals.sort_values(by='weight', ascending=False)
    return sortedAnimals[['name']]
