[Skip to main content](https://docs.tavily.com/welcome#content-area)

[Tavily Docs home page![light logo](https://mintcdn.com/tavilyai/HY1Rnt85q4usR4-R/logo/light.svg?fit=max&auto=format&n=HY1Rnt85q4usR4-R&q=85&s=c5c878011f13d458af0997f3a540eb4f)![dark logo](https://mintcdn.com/tavilyai/HY1Rnt85q4usR4-R/logo/dark.svg?fit=max&auto=format&n=HY1Rnt85q4usR4-R&q=85&s=1521677768a1f26b34a9ad86d04c62cc)](https://tavily.com/)

Search...

Ctrl KAsk AI

Search...

Navigation

[Home](https://docs.tavily.com/welcome) [Introduction](https://docs.tavily.com/documentation/about) [API & SDKs](https://docs.tavily.com/documentation/api-reference/introduction) [Ecosystem](https://docs.tavily.com/documentation/mcp) [Examples](https://docs.tavily.com/examples/use-cases/chat) [Changelog](https://docs.tavily.com/changelog) [Help](https://docs.tavily.com/documentation/help)

- [API Playground](https://app.tavily.com/playground)
- [Community](https://discord.gg/TPu2gkaWp2)
- [Blog](https://tavily.com/blog)

##### Welcome

# Build with Tavily

Your journey to state-of-the-art web search starts right here.

Installation

## Python SDK

```
pip install tavily-python
```

## JavaScript SDK

```
npm i @tavily/core
```

Try it now

- Search the web

- Extract webpages

- Crawl webpages

- Map webpages

- Create Research Task


Python

JavaScript

cURL

```
from tavily import TavilyClient

tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.search("Who is Leo Messi?")

print(response)
```

[Learn more about the Search API →](https://docs.tavily.com/documentation/api-reference/endpoint/search)

Python

JavaScript

cURL

```
from tavily import TavilyClient

tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.extract("https://en.wikipedia.org/wiki/Artificial_intelligence")

print(response)
```

[Learn more about the Extract API →](https://docs.tavily.com/documentation/api-reference/endpoint/extract)

Python

JavaScript

cURL

```
from tavily import TavilyClient

tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.crawl("https://docs.tavily.com", instructions="Find all pages on the Python SDK")

print(response)
```

[Learn more about the Crawl API →](https://docs.tavily.com/documentation/api-reference/endpoint/crawl)

Python

JavaScript

cURL

```
from tavily import TavilyClient

tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.map("https://docs.tavily.com")

print(response)
```

[Learn more about the Map API →](https://docs.tavily.com/documentation/api-reference/endpoint/map)

Python

JavaScript

cURL

```
from tavily import TavilyClient

tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.research("What are the latest developments in AI?")

print(response)
```

[Learn more about the Research API →](https://docs.tavily.com/documentation/api-reference/endpoint/research)

### Developer Resources

[**API Credits Overview** \\
\\
Learn how Tavily API credits work.](https://docs.tavily.com/documentation/api-credits)

[**Rate Limits** \\
\\
Understand Tavily’s rate limits and policies.](https://docs.tavily.com/documentation/rate-limits)

[**Playground** \\
\\
Try Tavily’s APIs interactively.](https://app.tavily.com/playground)

Question? [Contact Us](mailto:support@tavily.com)

Integration issues? [Join Community](https://community.tavily.com/)

Using LLMs? [Read LLMs.txt](https://docs.tavily.com/llms.txt)

Something not right? [Check Status](https://status.tavily.com/)

© Tavily [Privacy Policy](https://www.tavily.com/privacy)· [Website Terms of Use](https://www.tavily.com/website-terms)· [Platform Terms of Use](https://www.tavily.com/terms)· [Cookie Notice](https://www.tavily.com/cookie-policy)

[LinkedIn](https://www.linkedin.com/company/tavily)[Twitter](https://x.com/tavilyai)[GitHub](https://github.com/tavily-ai)[YouTube](https://www.youtube.com/@TavilyAI)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.