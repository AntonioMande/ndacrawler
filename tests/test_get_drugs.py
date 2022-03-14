

def test_herbal_human_drugs(drugs):
    # Data Extractors
    herbal_human_drugs = drugs["Herbal Human"]
    herbal_human_drugs.to_csv("Herbal Human.csv")
    assert True
