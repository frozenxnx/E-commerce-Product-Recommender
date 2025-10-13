import streamlit as st
import requests

CATEGORY_IMAGES = {
    "Electronics": [
        "https://plus.unsplash.com/premium_photo-1679079456083-9f288e224e96?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8RWxlY3Ryb25pY3N8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1603732551658-5fabbafa84eb?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8RWxlY3Ryb25pY3N8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1611186871348-b1ce696e52c9?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTR8fEVsZWN0cm9uaWNzfGVufDB8fDB8fHww&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjR8fEVsZWN0cm9uaWNzfGVufDB8fDB8fHww&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1620783770629-122b7f187703?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjN8fEVsZWN0cm9uaWNzfGVufDB8fDB8fHww&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1586062129117-08db958ba215?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzJ8fEVsZWN0cm9uaWNzfGVufDB8fDB8fHww&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1649859398731-d3c4ebca53fc?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzV8fEVsZWN0cm9uaWNzfGVufDB8fDB8fHww&auto=format&fit=crop&q=60&w=600"
    ],
    "Fashion": [
        "https://images.unsplash.com/photo-1571513800374-df1bbe650e56?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8RmFzaGlvbnxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=600",
        "https://plus.unsplash.com/premium_photo-1675186049419-d48f4b28fe7c?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8RmFzaGlvbnxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1603400521630-9f2de124b33b?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mzl8fEZhc2hpb258ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&q=60&w=600",
        "https://plus.unsplash.com/premium_photo-1664202526047-405824c633e7?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Njl8fEZhc2hpb258ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1558303522-d7a2bdfdbd82?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTE0fHxGYXNoaW9ufGVufDB8fDB8fHww&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1551232864-3f0890e580d9?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTE4fHxGYXNoaW9ufGVufDB8fDB8fHww&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1523398002811-999ca8dec234?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTMyfHxGYXNoaW9ufGVufDB8fDB8fHww&auto=format&fit=crop&q=60&w=600"
    ],
    "Home": [
        "https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8SG9tZXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=600",
        "https://plus.unsplash.com/premium_photo-1661964014750-963a28aeddea?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8SG9tZXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTR8fEhvbWV8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1484154218962-a197022b5858?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fEhvbWV8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1532372576444-dda954194ad0?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fEhvbWV8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1556020685-ae41abfc9365?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mjd8fEhvbWV8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1519643381401-22c77e60520e?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDh8fEhvbWV8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&q=60&w=600"
    ],
    "Sports": [
        "https://plus.unsplash.com/premium_photo-1685303469251-4ee0ea014bb3?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8U3BvcnRzfGVufDB8fDB8fHww&auto=format&fit=crop&q=60&w=600",
        "https://plus.unsplash.com/premium_photo-1676634832558-6654a134e920?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fFNwb3J0c3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1535131749006-b7f58c99034b?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjJ8fFNwb3J0c3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=600",
        "https://plus.unsplash.com/premium_photo-1666913667023-4bfd0f6cff0a?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDV8fFNwb3J0c3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1560089000-7433a4ebbd64?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NTZ8fFNwb3J0c3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1516820612845-a13894592046?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nzl8fFNwb3J0c3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1512746804203-e53e69406f93?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTAwfHxTcG9ydHN8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&q=60&w=600"
    ],
    "Beauty": [
        "https://images.unsplash.com/photo-1598528738936-c50861cc75a9?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8YmVhdXR5JTIwcHJvZHVjdHN8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1612817288484-6f916006741a?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8YmVhdXR5JTIwcHJvZHVjdHN8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&q=60&w=600",
        "https://plus.unsplash.com/premium_photo-1679046948726-72f7d53296c5?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8YmVhdXR5JTIwcHJvZHVjdHN8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fGJlYXV0eSUyMHByb2R1Y3RzfGVufDB8fDB8fHww&auto=format&fit=crop&q=60&w=600",
        "https://plus.unsplash.com/premium_photo-1684407616442-8d5a1b7c978e?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjF8fGJlYXV0eSUyMHByb2R1Y3RzfGVufDB8fDB8fHww&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1598460880248-71ec6d2d582b?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjZ8fGJlYXV0eSUyMHByb2R1Y3RzfGVufDB8fDB8fHww&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1556229010-aa3f7ff66b24?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzB8fGJlYXV0eSUyMHByb2R1Y3RzfGVufDB8fDB8fHww&auto=format&fit=crop&q=60&w=600"
    ],
    "Books": [
        "https://images.unsplash.com/photo-1512820790803-83ca734da794",
        "https://images.unsplash.com/photo-1519791883288-dc8bd696e667?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8ODh8fGJvb2t8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&q=60&w=600",
        "https://images.unsplash.com/photo-1577627444534-b38e16c9d796?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=736",
        "https://images.unsplash.com/photo-1506880018603-83d5b814b5a6?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1074",
        "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1074",
        "https://images.unsplash.com/photo-1543002588-bfa74002ed7e?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=687",
        "https://images.unsplash.com/photo-1544947950-fa07a98d237f?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=687"
    ],
"Groceries": [
    "https://images.unsplash.com/photo-1542838132-92c53300491e?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8Z3JvY2VyaWVzfGVufDB8fDB8fHww&auto=format&fit=crop&q=60&w=600",
    "https://media.istockphoto.com/id/613121170/photo/hot-7-grain-breakfast-cereal-with-yogurt-and-fresh-fruit.webp?a=1&b=1&s=612x612&w=0&k=20&c=sJ_1bIMQs9-hGiR0EzJ7huNQQ8KOd-A11xRUZg5hDvg=",
    "https://images.unsplash.com/photo-1614735241165-6756e1df61ab?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mjd8fGdyb2Nlcmllc3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=600",
    "https://images.unsplash.com/photo-1614907634002-65ac4cb74acb?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDd8fGdyb2Nlcmllc3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=600",
    "https://images.unsplash.com/photo-1585735633320-d24595a213a1?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NTB8fGdyb2Nlcmllc3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=600",
    "https://images.unsplash.com/photo-1691476093794-d923c08df935?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nzh8fGdyb2Nlcmllc3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=600",
    "https://images.unsplash.com/photo-1566454825481-4e48f80aa4d7?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTA4fHxncm9jZXJpZXN8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&q=60&w=600"
     ]
}

st.set_page_config(page_title="E-commerce Recommender", page_icon="🛍️", layout="wide")
st.title("🛒 E-commerce Product Recommender")
st.write("Get AI-powered product recommendations with Gemini explanations.")

# Helper for tag badges
def tag_badges(tags):
    color_map = {
        "bestseller": "#FFC107", "discount": "#4CAF50", "premium": "#00BCD4",
        "new": "#E91E63", "eco": "#8BC34A", "value": "#FFEB3B", "trending": "#9C27B0"
    }
    return " ".join(
        f"<span style='background-color:{color_map.get(tag.strip(), '#eee')};border-radius:8px;padding:2px 7px;margin:2px;font-size:0.89em;'>{tag}</span>"
        for tag in tags.split(",")
    )

user_id = st.text_input("Enter User ID", "1")
num_recs = st.slider("Number of recommendations", 3, 10, 5)

if st.button("Get Recommendations"):
    try:
        response = requests.get(f"http://127.0.0.1:8000/recommend?user_id={user_id}&k={num_recs}")
        data = response.json()

        st.subheader(f"Recommendations for User {user_id}")

        for item in data["recommendations"]:
            product = item["product"]
            explanation = item["explanation"]
            # Select a different image randomly for each product in the respective category list
            import random
            images_list = CATEGORY_IMAGES.get(product["category"], [f"https://via.placeholder.com/100x100.png?text={product['title'].replace(' ', '+')}"])
            img_url = random.choice(images_list)
            cols = st.columns([1, 3])
            with cols[0]:
                st.image(img_url, use_container_width=True)
            with cols[1]:
                st.markdown(f"### {product['title']}")
                st.markdown(tag_badges(product['tags']), unsafe_allow_html=True)
                st.markdown(f"**Category:** {product['category']}")
                st.markdown(f"**Price:** ${product['price']}")
                with st.expander("Why this product?"):
                    st.info(explanation)
            st.divider()

    except Exception as e:
        st.error(f"Error fetching recommendations: {e}")

st.markdown("""
<style>
.stButton > button {
    background: linear-gradient(90deg,#f7971e,#ffd200);
    color: #3f3d56;
    font-weight: bold;
    border-radius: 7px;
}
</style>
""", unsafe_allow_html=True)
