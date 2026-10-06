from app.services.recommendation_service import RecommendationEngine


def test_generate_recommendations():

    engine = RecommendationEngine()

    recommendations = engine.generate_recommendations(
        "customer support automation"
    )

    assert len(recommendations) == 3