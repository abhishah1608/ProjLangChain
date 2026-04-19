from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate


def getRestaurantandMenuDetails(cuisine_name):
    llm = ChatOpenAI(temperature=0.7)
    parser = JsonOutputParser()
    prompt = PromptTemplate.from_template(
        """
        give me top 2 rated Restaurants in the Toronto Downtown for the {cuisine} with it locations
        Return strictly in JSON format:
    {{
        "restaurants": [
            {{
                "name": "",
                "location": ""
            }}
        ]
    }}
        """)

    chain = prompt | llm | parser

    restaurant_names = chain.invoke({"cuisine": cuisine_name})

    restaurant_lists = [r['name'] for r in restaurant_names['restaurants']]

    restaurant_lists = [x.strip() for x in restaurant_lists]

    menu_prompt = PromptTemplate.from_template(
        """
        You are given a list of restaurants.
    
        {restaurants}
    
        provide top 10 rated vegetarian menus for each restaurants with ratings
    
        Return in JSON:
        {{
          "results": [ 
          "restaurant": "",
          "menu_items": ["", "", ""]
          ]
        }}
        """
    )

    menu_chain = menu_prompt | llm | parser

    output = []

    output = menu_chain.invoke({"restaurants": restaurant_lists})

    return output