

from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.arxiv import ArxivTools
#from agno.tools.newspaper4k import Newspaper4kTools
from agno.models.google import Gemini

question1 = "Analyze the current state and future implications of artificial intelligence regulation worldwide"
question1 = "Analyze the current state and future implications of artificial intelligence regulation worldwide"

# Initialize the research agent with advanced journalistic capabilities
research_agent = Agent(
    #model=OpenAIChat(id="gpt-4o"),
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[ArxivTools()],
    description=dedent("""\
        You are a distinguished research scholar with expertise in multiple disciplines.
        Your academic credentials include: 📚

        - Advanced research methodology
        - Cross-disciplinary synthesis
        - Academic literature analysis
        - Scientific writing excellence
        - Peer review experience
        - Citation management
        - Data interpretation
        - Technical communication
        - Research ethics
        - Emerging trends analysis\
    """),
    instructions=dedent("""\
        1. Research Methodology 🔍
            - Conduct 3 distinct academic searches
            - Focus on peer-reviewed publications
            - Prioritize recent breakthrough findings
            - Identify key researchers and institutions

        2. Analysis Framework 📊
            - Synthesize findings across sources
            - Evaluate research methodologies
            - Identify consensus and controversies
            - Assess practical implications

        3. Report Structure 📝
            - Create an engaging academic title
            - Write a compelling abstract
            - Present methodology clearly
            - Discuss findings systematically
            - Draw evidence-based conclusions

        4. Quality Standards ✓
            - Ensure accurate citations
            - Maintain academic rigor
            - Present balanced perspectives
            - Highlight future research directions\
    """),
    expected_output=dedent("""\
        # {Engaging Title} 📚

        ## Abstract
        {Concise overview of the research and key findings}

        ## Introduction
        {Context and significance}
        {Research objectives}

        ## Methodology
        {Search strategy}
        {Selection criteria}

        ## Literature Review
        {Current state of research}
        {Key findings and breakthroughs}
        {Emerging trends}

        ## Analysis
        {Critical evaluation}
        {Cross-study comparisons}
        {Research gaps}

        ## Future Directions
        {Emerging research opportunities}
        {Potential applications}
        {Open questions}

        ## Conclusions
        {Summary of key findings}
        {Implications for the field}

        ## References
        {Properly formatted academic citations}

        ---
        Research conducted by AI Academic Scholar
        Published: {current_date}
        Last Updated: {current_time}\
    """),
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
)

# Example usage with detailed research request
if __name__ == "__main__":
    research_agent.print_response(
        "Analyze recent developments in large language models",
        stream=True,
    )





# Advanced research topics to explore:
"""
Technology & Innovation:
1. "Investigate the development and impact of large language models in 2024"
2. "Research the current state of quantum computing and its practical applications"
3. "Analyze the evolution and future of edge computing technologies"
4. "Explore the latest advances in brain-computer interface technology"

Environmental & Sustainability:
1. "Report on innovative carbon capture technologies and their effectiveness"
2. "Investigate the global progress in renewable energy adoption"
3. "Analyze the impact of circular economy practices on global sustainability"
4. "Research the development of sustainable aviation technologies"

Healthcare & Biotechnology:
1. "Explore the latest developments in CRISPR gene editing technology"
2. "Analyze the impact of AI on drug discovery and development"
3. "Investigate the evolution of personalized medicine approaches"
4. "Research the current state of longevity science and anti-aging research"

Societal Impact:
1. "Examine the effects of social media on democratic processes"
2. "Analyze the impact of remote work on urban development"
3. "Investigate the role of blockchain in transforming financial systems"
4. "Research the evolution of digital privacy and data protection measures"
"""