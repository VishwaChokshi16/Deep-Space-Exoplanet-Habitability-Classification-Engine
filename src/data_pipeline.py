import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

def generate_astronomical_data():
    np.random.seed(42)
    n_samples = 2000
    data = {
        "Distance_from_Star_AU": np.random.uniform(0.1, 10.0, n_samples),
        "Planet_Mass_Earths": np.random.lognormal(mean=1.5, sigma=1.0, size=n_samples),
        "Stellar_Luminosity_Suns": np.random.uniform(0.2, 5.0, n_samples),
        "Atmospheric_Greenhouse_Factor": np.random.normal(1.0, 0.3, n_samples),
        "Habitability_Target": np.random.choice([0, 1], n_samples, p=[0.94, 0.06])
    }
    df = pd.DataFrame(data)
    df.loc[np.random.choice(df.index, 40), "Atmospheric_Greenhouse_Factor"] = np.nan
    return df

def build_space_pipeline():
    return Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="mean")),
        ("scaler", StandardScaler())
    ])