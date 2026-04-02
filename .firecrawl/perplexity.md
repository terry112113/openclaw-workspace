[Skip to main content](https://docs.perplexity.ai/docs/getting-started/overview#content-area)

[Perplexity home page![light logo](https://mintcdn.com/perplexity/gHf_T6roVjp3yaJv/logo/Perplexity_API_Platform.svg?fit=max&auto=format&n=gHf_T6roVjp3yaJv&q=85&s=07cab879ca2ce031bbc3da8b20f7ab90)![dark logo](https://mintcdn.com/perplexity/gHf_T6roVjp3yaJv/logo/Perplexity_API_Platform_Light.svg?fit=max&auto=format&n=gHf_T6roVjp3yaJv&q=85&s=416d5342d11094201b851dcf3eabdc9d)](https://docs.perplexity.ai/docs/getting-started/overview)

[Docs](https://docs.perplexity.ai/docs/getting-started/overview) [Cookbook](https://docs.perplexity.ai/docs/cookbook) [API Reference](https://docs.perplexity.ai/api-reference/agent-post)

Search...

Navigation

Search

Ctrl K

- [Community](https://community.perplexity.ai/)
- [Blog](https://research.perplexity.ai/articles)
- [Changelog](https://docs.perplexity.ai/docs/resources/changelog)

##### Getting Started

- [Overview](https://docs.perplexity.ai/docs/getting-started/overview)
- [Quickstart](https://docs.perplexity.ai/docs/getting-started/quickstart)
- [Pricing](https://docs.perplexity.ai/docs/getting-started/pricing)
- Tools & Integrations


##### Perplexity SDK

- [Quickstart](https://docs.perplexity.ai/docs/sdk/overview)
- Guides


##### Agent API

- [Quickstart](https://docs.perplexity.ai/docs/agent-api/quickstart)
- Models & Configuration

- Features

- [OpenAI Compatibility](https://docs.perplexity.ai/docs/agent-api/openai-compatibility)

##### Search API

- [Quickstart](https://docs.perplexity.ai/docs/search/quickstart)
- Filters

- [Best Practices](https://docs.perplexity.ai/docs/search/best-practices)

##### Sonar API

- [Quickstart](https://docs.perplexity.ai/docs/sonar/quickstart)
- [Models](https://docs.perplexity.ai/docs/sonar/models)
- Features


##### Embeddings API

- [Quickstart](https://docs.perplexity.ai/docs/embeddings/quickstart)
- [Standard Embeddings](https://docs.perplexity.ai/docs/embeddings/standard-embeddings)
- [Contextualized Embeddings](https://docs.perplexity.ai/docs/embeddings/contextualized-embeddings)
- [Best Practices](https://docs.perplexity.ai/docs/embeddings/best-practices)

##### Admin & Management

- [API Groups & Billing](https://docs.perplexity.ai/docs/getting-started/api-groups)
- [API Key Management](https://docs.perplexity.ai/docs/admin/api-key-management)
- [Rate Limits & Usage Tiers](https://docs.perplexity.ai/docs/admin/rate-limits-usage-tiers)

##### Resources

- [API Roadmap](https://docs.perplexity.ai/docs/resources/feature-roadmap)
- [Privacy & Security](https://docs.perplexity.ai/docs/resources/privacy-security)
- [Frequently Asked Questions](https://docs.perplexity.ai/docs/resources/faq)
- [System Status](https://docs.perplexity.ai/docs/resources/status)
- [Changelog](https://docs.perplexity.ai/docs/resources/changelog)
- [Get in Touch](https://docs.perplexity.ai/docs/resources/discussions)
- [Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers)

![Perplexity API Platform](https://docs.perplexity.ai/logo/Perplexity_API_Platform.svg)![Perplexity API Platform](https://docs.perplexity.ai/logo/Perplexity_API_Platform_Light.svg)

Power your products with unparalleled real-time, web-wide research and Q&A capabilities.

Quickstart GuideGetting started is simple and fast—make your first API call within minutes.

[Get Started](https://docs.perplexity.ai/docs/getting-started/quickstart) [Get Your API Key](https://console.perplexity.ai/)

Python

Typescript

cURL

```
from perplexity import Perplexity

client = Perplexity()

search = client.search.create(
    query=[\
      "What is Comet Browser?",\
      "Perplexity AI",\
      "Perplexity Changelog"\
    ]
)

for result in search.results:
    print(f"{result.title}: {result.url}")
```

[Get Started](https://console.perplexity.ai/)

## Available APIs

[![Agent API](https://mintcdn.com/perplexity/38tmR5FPCzFbGyn-/docs/assets/images/overview/Agent.jpg?fit=max&auto=format&n=38tmR5FPCzFbGyn-&q=85&s=738ba1d84eb63748cf3e38c2fec0a6e7)](https://docs.perplexity.ai/docs/agent-api/quickstart)[Agent API](https://docs.perplexity.ai/docs/agent-api/quickstart)

Access third-party models with web search tools and presets.

[![Search API](https://mintcdn.com/perplexity/38tmR5FPCzFbGyn-/docs/assets/images/overview/Search.jpg?fit=max&auto=format&n=38tmR5FPCzFbGyn-&q=85&s=84d08a7c89feb2ff330f8bf6e9d814cc)](https://docs.perplexity.ai/docs/search/quickstart)[Search API](https://docs.perplexity.ai/docs/search/quickstart)

Get raw, ranked web search results with advanced filtering and real-time data.

[![Embeddings API](https://mintcdn.com/perplexity/38tmR5FPCzFbGyn-/docs/assets/images/overview/Embeddings.jpg?fit=max&auto=format&n=38tmR5FPCzFbGyn-&q=85&s=921a7fa48c1654a77ff21b1287f95369)](https://docs.perplexity.ai/docs/embeddings/quickstart)[Embeddings API](https://docs.perplexity.ai/docs/embeddings/quickstart)

Generate high-quality embeddings for semantic search and RAG pipelines.

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

What is the Agent API?Which Agent API model should I use?How do I create an API key?

![Perplexity API Platform](https://docs.perplexity.ai/logo/Perplexity_API_Platform.svg)

![Agent API](https://mintcdn.com/perplexity/38tmR5FPCzFbGyn-/docs/assets/images/overview/Agent.jpg?w=2500&fit=max&auto=format&n=38tmR5FPCzFbGyn-&q=85&s=28410a9423254435d57d324aa0668534)

![Search API](https://mintcdn.com/perplexity/38tmR5FPCzFbGyn-/docs/assets/images/overview/Search.jpg?w=2500&fit=max&auto=format&n=38tmR5FPCzFbGyn-&q=85&s=06f9463ed1d87cdb849378aa53afdf41)

![Embeddings API](https://mintcdn.com/perplexity/38tmR5FPCzFbGyn-/docs/assets/images/overview/Embeddings.jpg?w=2500&fit=max&auto=format&n=38tmR5FPCzFbGyn-&q=85&s=14eb76017cab64fb61e1f5e8533b0937)