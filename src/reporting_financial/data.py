import pandas as pd


DATA_URL = "https://minio.lab.sspcloud.fr/fabienhos/td-reporting-financial/financial_data.parquet"


def load_data(url: str = DATA_URL) -> pd.DataFrame:
    """
    Charge les données financières depuis le fichier Parquet.
    """
    df = pd.read_parquet(url)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    score_mapping = {"V": 1, "O": 2, "R": 3}

    df["score_num"] = df["score"].map(score_mapping)
    df["score_prev_num"] = df["score_prev"].map(score_mapping)

    # Gestion des NaN → on remplace par le score actuel (choix simple et logique)
    df["score_prev_num"] = df["score_prev_num"].fillna(df["score_num"])

    df["score_evolution"] = df["score_num"] - df["score_prev_num"]

    risk_mapping = {1: "Faible", 2: "Moyen", 3: "Élevé"}
    df["risk_level"] = df["score_num"].map(risk_mapping)

    df["score_status"] = df["score_evolution"].apply(
        lambda x: "Hausse" if x > 0 else "Baisse" if x < 0 else "Stable"
    )

    return df
    

