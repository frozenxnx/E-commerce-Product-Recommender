from fastapi import FastAPI
from app.recommender import recommend_products
from app.llm_explainer import explain_recommendation

app = FastAPI(title="E-commerce Product Recommender")

@app.get("/recommend")
def get_recommendations(user_id: int, k: int = 5):
    recommendations = recommend_products(user_id, k)
    result = []
    for p in recommendations:
        explanation = explain_recommendation(user_id, p)
        result.append({"product": p, "explanation": explanation})
    return {"user_id": user_id, "recommendations": result}
