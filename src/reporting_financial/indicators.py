import pandas as pd


def compute_global_indicators(df: pd.DataFrame) -> pd.DataFrame:
    indicators = {
        "Nombre total de clients": len(df),
        "Score moyen": round(df["score_num"].mean(), 2),
        "Score précédent moyen": round(df["score_prev_num"].mean(), 2),
        "Évolution moyenne du score": round(df["score_evolution"].mean(), 2),
        "Taux de dossiers complets (%)": round(df["drc_complet"].mean() * 100, 2),
        "Nombre de clients à risque élevé": int((df["risk_level"] == "Élevé").sum()),
        "Nombre de scores en hausse": int((df["score_status"] == "Hausse").sum()),
    }

    return pd.DataFrame(indicators.items(), columns=["Indicateur", "Valeur"])


def compute_client_type_indicators(df: pd.DataFrame) -> pd.DataFrame:
    result = (
        df.groupby("type_client")
        .agg(
            nombre_clients=("type_client", "count"),
            score_moyen=("score_num", "mean"),
            taux_dossiers_complets=("drc_complet", "mean"),
        )
        .reset_index()
    )

    result["score_moyen"] = result["score_moyen"].round(2)
    result["taux_dossiers_complets"] = (result["taux_dossiers_complets"] * 100).round(2)

    return result


def compute_agent_indicators(df: pd.DataFrame) -> pd.DataFrame:
    result = (
        df.groupby("id_agent")
        .agg(
            nombre_clients=("id_agent", "count"),
            score_moyen=("score_num", "mean"),
            dossiers_complets=("drc_complet", "sum"),
        )
        .reset_index()
        .sort_values("nombre_clients", ascending=False)
    )

    result["score_moyen"] = result["score_moyen"].round(2)

    return result
    