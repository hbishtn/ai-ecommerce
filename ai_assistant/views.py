from django.shortcuts import render
from groq import Groq
from products.models import Product
import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def ai_search(request):

    response_text = ""

    if request.method == "POST":
        user_prompt = request.POST.get("prompt")
        products = Product.objects.all()
        product_data = ""

        for product in products:

            product_data += f"""

            Product Name: {product.name}

            Description: {product.description}

            Price: ₹{product.price}

        """

        user_prompt = request.POST.get("prompt")

        try:

            chat_completion = client.chat.completions.create(

                messages=[
                    {
                        "role": "user",
                        "content": f"""

                        You are an AI ecommerce assistant.

                        These are available products:

                        {product_data}

                        User Question:
                        {user_prompt}

                        Recommend products only from available products.

                        """,
                    }
                ],

                model="llama-3.3-70b-versatile",

            )

            response_text = chat_completion.choices[0].message.content

        except Exception as e:

            response_text = str(e)

    return render(

        request,

        "ai_assistant/ai_search.html",

        {

            "response": response_text

        }

    )



    