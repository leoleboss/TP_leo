from src.reporting_financial.data import load_data, clean_data
from src.reporting_financial.indicators import (
    compute_global_indicators,
    compute_client_type_indicators,
    compute_agent_indicators,
)
from src.reporting_financial.report import create_report


def main():
    # 1. Charger les données
    df = load_data()

    # 2. Nettoyer les données
    df = clean_data(df)

    # 3. Calculer les indicateurs
    global_indicators = compute_global_indicators(df)
    client_type_indicators = compute_client_type_indicators(df)
    agent_indicators = compute_agent_indicators(df)

    # 4. Générer le rapport Excel
    create_report(
        df=df,
        global_indicators=global_indicators,
        client_type_indicators=client_type_indicators,
        agent_indicators=agent_indicators,
    )


if __name__ == "__main__":
    main()
    