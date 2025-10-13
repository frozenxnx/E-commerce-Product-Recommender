import pandas as pd
import random

# Load product and user data
products = pd.read_csv("data/products.csv")
user_behavior = pd.read_csv("data/user_behavior.csv")


def get_user_preferences(user_id: int):
    """Return the list of products the user has interacted with."""
    user_data = user_behavior[user_behavior["user_id"] == user_id]
    if user_data.empty:
        return pd.DataFrame()  # Return empty DataFrame instead of list
    viewed = user_data.merge(products, left_on="product_id", right_on="id")
    return viewed


def recommend_products(user_id: int, k: int = 5):
    """Simple content-based recommender: match categories and tags."""
    user_products = get_user_preferences(user_id)

    # Only check if the DataFrame is empty
    if user_products.empty:
        return products.sample(k).to_dict(orient="records")

    # Get preferred categories and tags
    top_category = user_products["category"].mode()[0]
    user_tags = ",".join(user_products["tags"].values).split(",")

    # Filter by category and tags
    filtered = products[products["category"] == top_category].copy()
    filtered["tag_score"] = filtered["tags"].apply(
        lambda x: sum(tag in user_tags for tag in x.split(","))
    )

    # Exclude already viewed products
    viewed_ids = set(user_products["id"].values)
    filtered = filtered[~filtered["id"].isin(viewed_ids)]

    if filtered.empty:
        return products.sample(k).to_dict(orient="records")

    recommendations = filtered.sort_values("tag_score", ascending=False).head(k)
    return recommendations.to_dict(orient="records")
