<div align="center">

# MCP Traders

### Autonomous AI Trading Agents Powered by Model Context Protocol

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Gradio](https://img.shields.io/badge/Gradio-5.0+-FF7C00?style=for-the-badge&logo=gradio&logoColor=white)](https://gradio.app)
[![OpenAI](https://img.shields.io/badge/OpenAI_Agents-SDK-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<br/>

*A sophisticated multi-agent trading simulation platform featuring four autonomous AI traders, each embodying distinct investment philosophies inspired by legendary investors.*

<br/>

[Features](#features) | [Architecture](#architecture) | [Installation](#installation) | [Configuration](#configuration) | [Usage](#usage) | [API Reference](#api-reference)

---

</div>

## Overview

MCP Traders is an advanced trading simulation platform that demonstrates the power of **agentic AI** combined with the **Model Context Protocol (MCP)**. The system deploys four autonomous trading agents, each powered by large language models, capable of conducting market research, analyzing opportunities, and executing trades based on their unique investment strategies.

Unlike traditional algorithmic trading systems that rely on predefined rules, MCP Traders leverages the reasoning capabilities of modern LLMs to make nuanced investment decisions, adapt to market conditions, and learn from experience through persistent memory systems.

---

## Features

<table>
<tr>
<td width="50%">

### Autonomous Decision Making
- Real-time market analysis using LLM reasoning
- Strategy-driven investment decisions
- Adaptive behavior based on market conditions
- Multi-turn reasoning with tool usage

</td>
<td width="50%">

### Model Context Protocol Integration
- Modular tool architecture via MCP servers
- Account management tools
- Market data integration
- Web search capabilities for research

</td>
</tr>
<tr>
<td width="50%">

### Real-Time Dashboard
- Live portfolio tracking with Plotly charts
- Transaction history and rationale display
- Color-coded activity logs
- Auto-refreshing interface

</td>
<td width="50%">

### Persistent Memory
- LibSQL-based knowledge graphs per agent
- Cross-session learning and recall
- Entity relationship storage
- Shared knowledge base between agents

</td>
</tr>
</table>

---

## Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              MCP TRADERS PLATFORM                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                         TRADING FLOOR                                │   │
│  │                    (trading_floor.py)                                │   │
│  │                                                                      │   │
│  │   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐          │   │
│  │   │  WARREN  │  │  GEORGE  │  │   RAY    │  │  CATHIE  │          │   │
│  │   │  Value   │  │  Macro   │  │Systematic│  │  Crypto  │          │   │
│  │   │ Investor │  │ Trader   │  │ Investor │  │   ETFs   │          │   │
│  │   └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘          │   │
│  │        │             │             │             │                 │   │
│  │        └─────────────┴──────┬──────┴─────────────┘                 │   │
│  │                             │                                       │   │
│  └─────────────────────────────┼───────────────────────────────────────┘   │
│                                │                                            │
│  ┌─────────────────────────────▼───────────────────────────────────────┐   │
│  │                      AGENT FRAMEWORK                                 │   │
│  │                    (OpenAI Agents SDK)                               │   │
│  │                                                                      │   │
│  │  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐             │   │
│  │  │   TRADER    │───▶│ RESEARCHER  │───▶│     LLM     │             │   │
│  │  │   AGENT     │    │   AGENT     │    │   (Gemini)  │             │   │
│  │  └─────────────┘    └─────────────┘    └─────────────┘             │   │
│  │                                                                      │   │
│  └──────────────────────────────┬───────────────────────────────────────┘   │
│                                 │                                           │
│  ┌──────────────────────────────▼───────────────────────────────────────┐  │
│  │                        MCP SERVER LAYER                               │  │
│  │                                                                       │  │
│  │  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐         │  │
│  │  │   ACCOUNTS     │  │    MARKET      │  │   RESEARCHER   │         │  │
│  │  │    SERVER      │  │    SERVER      │  │    SERVERS     │         │  │
│  │  │                │  │                │  │                │         │  │
│  │  │ - get_balance  │  │ - share_price  │  │ - web_search   │         │  │
│  │  │ - buy_shares   │  │ - market_data  │  │ - fetch_url    │         │  │
│  │  │ - sell_shares  │  │ - indicators   │  │ - memory_store │         │  │
│  │  │ - holdings     │  │                │  │ - memory_read  │         │  │
│  │  └───────┬────────┘  └───────┬────────┘  └───────┬────────┘         │  │
│  │          │                   │                   │                   │  │
│  └──────────┼───────────────────┼───────────────────┼───────────────────┘  │
│             │                   │                   │                      │
│  ┌──────────▼───────────────────▼───────────────────▼───────────────────┐  │
│  │                         DATA LAYER                                    │  │
│  │                                                                       │  │
│  │  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐              │  │
│  │  │ accounts.db │    │ Polygon API │    │  memory/*.db │              │  │
│  │  │  (SQLite)   │    │             │    │   (LibSQL)   │              │  │
│  │  └─────────────┘    └─────────────┘    └─────────────┘              │  │
│  │                                                                       │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Component Description

| Component | File | Description |
|-----------|------|-------------|
| **Trading Floor** | `trading_floor.py` | Orchestrates all trading agents, manages scheduling and execution cycles |
| **Trader Agent** | `traders.py` | Individual AI trader implementation with strategy execution |
| **Accounts Server** | `accounts_server.py` | MCP server providing account management tools |
| **Market Server** | `market_server.py` | MCP server for stock price lookups |
| **Dashboard** | `app.py` | Gradio-based real-time monitoring interface |
| **Database** | `database.py` | SQLite persistence layer for accounts and logs |
| **Market Data** | `market.py` | Polygon.io API integration for market data |

---

## Agent Flow

### Trading Cycle Execution

```
                                    START
                                      │
                                      ▼
                        ┌─────────────────────────┐
                        │   Initialize Traders    │
                        │   (Load Strategies)     │
                        └───────────┬─────────────┘
                                    │
                                    ▼
                        ┌─────────────────────────┐
                        │   Check Market Status   │
                        │   (Open/Closed)         │
                        └───────────┬─────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
            [Market Open]                   [Market Closed]
                    │                               │
                    ▼                               ▼
        ┌───────────────────┐           ┌───────────────────┐
        │  Run All Traders  │           │   Skip Iteration  │
        │   (Parallel)      │           │                   │
        └─────────┬─────────┘           └─────────┬─────────┘
                  │                               │
                  ▼                               │
        ┌───────────────────┐                     │
        │  Connect to MCP   │                     │
        │     Servers       │                     │
        └─────────┬─────────┘                     │
                  │                               │
                  ▼                               │
        ┌───────────────────┐                     │
        │  Read Account &   │                     │
        │    Strategy       │                     │
        └─────────┬─────────┘                     │
                  │                               │
                  ▼                               │
        ┌───────────────────┐                     │
        │  Execute Agent    │                     │
        │  (LLM Reasoning)  │                     │
        └─────────┬─────────┘                     │
                  │                               │
        ┌─────────┴─────────┐                     │
        │                   │                     │
        ▼                   ▼                     │
   [Research]          [Trade]                    │
        │                   │                     │
        ▼                   ▼                     │
┌───────────────┐  ┌───────────────┐             │
│ Web Search    │  │ Buy/Sell      │             │
│ Fetch URLs    │  │ Shares        │             │
│ Store Memory  │  │               │             │
└───────┬───────┘  └───────┬───────┘             │
        │                   │                     │
        └─────────┬─────────┘                     │
                  │                               │
                  ▼                               │
        ┌───────────────────┐                     │
        │   Log Activity    │                     │
        │   Update Account  │                     │
        └─────────┬─────────┘                     │
                  │                               │
                  └───────────────┬───────────────┘
                                  │
                                  ▼
                        ┌─────────────────────────┐
                        │   Sleep N Minutes       │
                        │   (Default: 60)         │
                        └───────────┬─────────────┘
                                    │
                                    ▼
                                 [REPEAT]
```

### Agent Decision Process

```
┌─────────────────────────────────────────────────────────────────────┐
│                     AGENT DECISION PROCESS                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. CONTEXT GATHERING                                               │
│     ┌──────────────────────────────────────────────────────────┐   │
│     │  • Load investment strategy from account                  │   │
│     │  • Retrieve current holdings and balance                  │   │
│     │  • Query memory for relevant past knowledge               │   │
│     └──────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  2. RESEARCH PHASE                                                  │
│     ┌──────────────────────────────────────────────────────────┐   │
│     │  • Delegate to Researcher Agent                           │   │
│     │  • Search web for market news and opportunities           │   │
│     │  • Fetch relevant financial data                          │   │
│     │  • Store new knowledge in memory graph                    │   │
│     └──────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  3. ANALYSIS PHASE                                                  │
│     ┌──────────────────────────────────────────────────────────┐   │
│     │  • Evaluate opportunities against strategy                │   │
│     │  • Check stock prices and market conditions               │   │
│     │  • Calculate position sizes based on balance              │   │
│     │  • Assess risk/reward ratios                              │   │
│     └──────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  4. EXECUTION PHASE                                                 │
│     ┌──────────────────────────────────────────────────────────┐   │
│     │  • Execute buy/sell orders via MCP tools                  │   │
│     │  • Record transaction rationale                           │   │
│     │  • Update portfolio state                                 │   │
│     │  • Log activity for monitoring                            │   │
│     └──────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## The Four Traders

<table>
<tr>
<td width="25%" align="center">
<h3>WARREN</h3>
<strong>Value Investor</strong>
<br/><br/>
<em>Inspired by Warren Buffett</em>
<br/><br/>
Focuses on identifying high-quality companies trading below intrinsic value. Employs meticulous fundamental analysis, prioritizes strong cash flows, competent management, and sustainable competitive advantages. Maintains long-term positions through market fluctuations.
</td>
<td width="25%" align="center">
<h3>GEORGE</h3>
<strong>Macro Trader</strong>
<br/><br/>
<em>Inspired by George Soros</em>
<br/><br/>
Aggressive macro trader seeking significant market mispricings. Analyzes large-scale economic and geopolitical events for investment opportunities. Employs contrarian strategies, betting boldly against prevailing sentiment when analysis suggests imbalance.
</td>
<td width="25%" align="center">
<h3>RAY</h3>
<strong>Systematic Investor</strong>
<br/><br/>
<em>Inspired by Ray Dalio</em>
<br/><br/>
Applies systematic, principles-based approach rooted in macroeconomic insights. Diversifies broadly across asset classes using risk parity strategies. Monitors economic indicators, central bank policies, and cycles to manage risk and preserve capital.
</td>
<td width="25%" align="center">
<h3>CATHIE</h3>
<strong>Crypto ETF Specialist</strong>
<br/><br/>
<em>Inspired by Cathie Wood</em>
<br/><br/>
Aggressively pursues disruptive innovation opportunities, focusing on Crypto ETFs. Accepts higher volatility for exceptional return potential. Monitors technological breakthroughs, regulatory changes, and market sentiment in the crypto space.
</td>
</tr>
</table>

---

## Installation

### Prerequisites

- Python 3.12 or higher
- Node.js 18+ (for MCP servers)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/anikets81/MCP_Traders.git
cd MCP_Traders
```

### Step 2: Create Virtual Environment

```bash
# Using uv (recommended)
uv venv
uv pip install -r requirements.txt

# Or using pip
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables

Create a `.env` file in the project root:

```env
# AI Model API Key (Required)
GOOGLE_API_KEY=your_google_api_key

# Market Data (Required)
POLYGON_API_KEY=your_polygon_api_key

# Web Search (Required)
BRAVE_API_KEY=your_serper_api_key

# Optional Configuration
RUN_EVERY_N_MINUTES=60
RUN_EVEN_WHEN_MARKET_IS_CLOSED=true
USE_MANY_MODELS=false
```

### Step 4: Initialize Accounts

```bash
python reset.py
```

---

## Configuration

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `GOOGLE_API_KEY` | Yes | - | Google AI API key for Gemini models |
| `POLYGON_API_KEY` | Yes | - | Polygon.io API key for market data |
| `BRAVE_API_KEY` | Yes | - | Search API key (Serper API) |
| `RUN_EVERY_N_MINUTES` | No | `60` | Trading cycle interval in minutes |
| `RUN_EVEN_WHEN_MARKET_IS_CLOSED` | No | `false` | Run agents outside market hours |
| `USE_MANY_MODELS` | No | `false` | Use different LLMs per trader |
| `POLYGON_PLAN` | No | `free` | Polygon subscription: `free`, `paid`, `realtime` |

### Model Configuration

When `USE_MANY_MODELS=true`, each trader uses a different LLM:

| Trader | Model | Provider |
|--------|-------|----------|
| Warren | GPT-4.1 Mini | OpenAI |
| George | DeepSeek Chat | DeepSeek |
| Ray | Gemini 2.5 Flash | Google |
| Cathie | Grok 3 Mini | xAI |

---

## Usage

### Running the Dashboard

```bash
python app.py
```

Access the dashboard at `http://localhost:7860`

### Running the Trading Agents

```bash
python trading_floor.py
```

The agents will execute trading cycles at the configured interval.

### Running Both Services

**Terminal 1 - Dashboard:**
```bash
python app.py
```

**Terminal 2 - Trading Agents:**
```bash
python trading_floor.py
```

---

## API Reference

### MCP Tools - Accounts Server

| Tool | Parameters | Description |
|------|------------|-------------|
| `get_balance` | `name: str` | Returns current cash balance |
| `get_holdings` | `name: str` | Returns dictionary of stock holdings |
| `buy_shares` | `name: str, symbol: str, quantity: int, rationale: str` | Executes buy order |
| `sell_shares` | `name: str, symbol: str, quantity: int, rationale: str` | Executes sell order |
| `change_strategy` | `name: str, strategy: str` | Updates investment strategy |

### MCP Tools - Market Server

| Tool | Parameters | Description |
|------|------------|-------------|
| `lookup_share_price` | `symbol: str` | Returns current stock price |

### MCP Resources

| Resource URI | Description |
|--------------|-------------|
| `accounts://accounts_server/{name}` | Full account report including holdings, transactions, P&L |
| `accounts://strategy/{name}` | Current investment strategy text |

---

## Project Structure

```
MCP_Traders/
├── app.py                 # Gradio dashboard application
├── trading_floor.py       # Main orchestrator for trading agents
├── traders.py             # Trader agent implementation
├── accounts.py            # Account data model and operations
├── accounts_server.py     # MCP server for account tools
├── accounts_client.py     # MCP client utilities
├── market.py              # Market data fetching (Polygon API)
├── market_server.py       # MCP server for market data tools
├── mcp_params.py          # MCP server configurations
├── templates.py           # Agent instruction templates
├── tracers.py             # Logging and tracing utilities
├── database.py            # SQLite database operations
├── util.py                # CSS and utility functions
├── reset.py               # Account initialization script
├── requirements.txt       # Python dependencies
├── accounts.db            # SQLite database (generated)
└── memory/                # Agent memory databases
    ├── Warren.db
    ├── George.db
    ├── Ray.db
    └── Cathie.db
```

---

## Database Schema

### Accounts Table

```sql
CREATE TABLE accounts (
    name TEXT PRIMARY KEY,
    account TEXT  -- JSON blob containing full account data
);
```

### Logs Table

```sql
CREATE TABLE logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    datetime DATETIME,
    type TEXT,      -- trace, agent, function, generation, response, account
    message TEXT
);
```

### Market Table

```sql
CREATE TABLE market (
    date TEXT PRIMARY KEY,
    data TEXT  -- JSON blob of all stock prices for the date
);
```

---

## Deployment

### Docker

```bash
docker build -t mcp-traders .
docker run -p 7860:7860 --env-file .env mcp-traders
```

### Hugging Face Spaces

The project is configured for deployment on Hugging Face Spaces with Gradio SDK.

### Railway / Render

Use the provided `Procfile` and `requirements.txt` for platform deployment.

---

## Monitoring

### Dashboard Features

- **Portfolio Value**: Real-time total portfolio value with P&L indicator
- **Value Chart**: Historical portfolio value over time (Plotly)
- **Holdings Table**: Current stock positions with quantities
- **Transactions Table**: Complete trade history with rationale
- **Activity Logs**: Color-coded real-time activity feed

### Log Types

| Type | Color | Description |
|------|-------|-------------|
| `trace` | Light Blue | Agent lifecycle events |
| `agent` | Cyan | Agent-level operations |
| `function` | Green | Tool/function calls |
| `generation` | Yellow | LLM generation events |
| `response` | Magenta | LLM responses |
| `account` | Red | Account modifications |

---

## Contributing

Contributions are welcome. Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **OpenAI** - Agents SDK framework
- **Anthropic** - Model Context Protocol specification
- **Google** - Gemini AI models
- **Polygon.io** - Market data API
- **Gradio** - Dashboard framework

---

<div align="center">

**Built with the Model Context Protocol**

[Report Bug](https://github.com/anikets81/MCP_Traders/issues) | [Request Feature](https://github.com/anikets81/MCP_Traders/issues)

</div>
