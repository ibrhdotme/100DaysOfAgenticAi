"""
Creating a basic Web search agent - Code from https://docs.phidata.com/
"""

###########################
# save this as web_agent.py
############################

from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo

web_agent = Agent(
    name="Web Agent",
    model=Gemini(id="gemini-2.0-flash-exp",api_key="REDACTED - ACTUAL API KEY GOES HERE"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

web_agent.print_response("Find me if there are any limitations on using gemini api for free? find me limiations for 1.5 pro and 2.0 flash", stream=True)

#################################
# Run it with python web_agent.py
#################################

"""
Creating a basic multi agent setup - Code from https://docs.phidata.com/
"""

############################
# save this as agent_team.py
############################


from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools


web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=Gemini(id="gemini-2.0-flash-exp",api_key="REDACTED - ACTUAL API KEY GOES HERE"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Gemini(id="gemini-2.0-flash-exp",api_key="REDACTED - ACTUAL API KEY GOES HERE"),
    tools=[YFinanceTools(enable_all=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    model=Gemini(id="gemini-2.0-flash-exp",api_key="REDACTED - ACTUAL API KEY GOES HERE"),
    team=[web_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("find me top semi conductor stocks using web and then find current price with finanace ones that are top recomended",stream=True)

###############################
# run with python agent_team.py
###############################