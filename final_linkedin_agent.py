from agents import Agent, Runner, function_tool, set_tracing_export_api_key
import asyncio
import agentops
import os
from dotenv import load_dotenv
import requests
from rss_script import rss_extract
import prompts
import streamlit as st

# Load environment variables from .env file
load_dotenv()

openai_key = os.environ.get("OPENAI_API_KEY")
agentops_key = os.environ.get("AGENTOPS_API_KEY")

os.environ["OPENAI_API_KEY"] = openai_key

set_tracing_export_api_key(openai_key)

## Functions
@function_tool
def get_html_from_url(url: str) -> str:
    """Fetches the HTML content from the given URL
        url: URL of the website
        return: HTML content of the website
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an error for bad status codes
        return response.text  # Returns raw HTML as a string
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return ""

def generate_html_table(data):
    """Generates an HTML table from a list of dictionaries."""
    if not data:
        return "<p>No data available</p>"

    table_html = "<table style='width:100%; border-collapse: collapse;'>"
    
    # Table Header
    table_html += "<tr style='background-color: #3498db; color: white;'>"
    for key in data[0].keys():
        table_html += f"<th style='padding: 10px; border: 1px solid black;'>{key}</th>"
    table_html += "</tr>"
    
    # Table Rows
    for row in data:
        table_html += "<tr>"
        for value in row.values():
            table_html += f"<td style='padding: 10px; border: 1px solid black;'>{value}</td>"
        table_html += "</tr>"

    table_html += "</table>"
    return table_html

# Initialize AgentOps (AgentOps API Key from .env)
agentops.init(agentops_key)

instructions = "You are a helpful assistant"
agent_name2 = "LinkedIn Assistant"

html_parsing_agent = Agent(
    name=agent_name2,
    instructions=prompts.prompt1(),
    tools=[get_html_from_url],
)

agent_name3 = "LinkedIn Assistant"
linkedin_agent = Agent(name=agent_name3, instructions=instructions)


agent_name4 = "LinkedIn Post Analyst"
post_analysis_agent = Agent(name="agent_name4", instructions=instructions)

top_n_articles = rss_extract(3)

# print("Here")
# print(top_n_articles)

async def main():
    for article in top_n_articles:
        blog_content = await Runner.run(html_parsing_agent, input="Here is the URL:" + article['link'])

        linkedin_post = await Runner.run(linkedin_agent, prompts.prompt2(blog_content.final_output))

        analysis = await Runner.run(post_analysis_agent, prompts.prompt3(blog_content.final_output, linkedin_post.final_output))

        article['linked_in_post'] = linkedin_post.final_output
        article['analysis'] = analysis.final_output

if __name__ == "__main__":
    asyncio.run(main())

    st.title("Reusable HTML Table in Streamlit")

    # Render table using imported function
    st.markdown(generate_html_table(top_n_articles), unsafe_allow_html=True)

    # print("Output")

    # print(top_n_articles)

    # for i in top_n_articles:
    #     print(i)