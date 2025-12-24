# HR Agent System

> **HR Agent System with Microsoft 365 Agent Toolkit and Teams App Integration**
> 
> A Python-based multi-agent system for comprehensive HR management, built with Microsoft 365 integration and AI-powered automation.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Agents](#agents)
- [Teams Integration](#teams-integration)
- [API Documentation](#api-documentation)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

The HR Agent System is an intelligent, multi-agent platform designed to automate and streamline HR operations. Built on Microsoft 365 Agent Toolkit, it leverages AI and semantic understanding to handle recruitment, employee onboarding, performance management, and leave management through natural language interactions.

### Key Technologies

- **Microsoft 365 Agent SDK**: Core agent framework
- **Azure AI Services**: Advanced AI capabilities
- **Microsoft Graph API**: Microsoft 365 integration
- **Teams Bot Framework**: Conversational AI interface
- **LangChain & Semantic Kernel**: Agent orchestration
- **FastAPI**: REST API backend
- **Vector Databases**: RAG implementation

## ✨ Features

### 🤖 Intelligent Agents

- **Recruitment Agent**: Job posting, candidate screening, interview scheduling
- **Onboarding Agent**: Automated onboarding workflows, document management
- **Performance Agent**: Performance reviews, goal tracking, feedback collection
- **Leave Management Agent**: Leave requests, approval workflows, balance tracking

### 🔗 Microsoft 365 Integration

- Seamless Teams integration for conversational interactions
- Microsoft Graph API for calendar, email, and SharePoint access
- Azure AD authentication and authorization
- OneDrive document storage

### 🧠 AI Capabilities

- Natural language understanding
- Context-aware responses
- RAG (Retrieval-Augmented Generation) for knowledge base
- Multi-agent collaboration
- Automated workflow orchestration

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Teams Interface                       │
│  (Bot Framework + Adaptive Cards)                       │
└────────────────┬────────────────────────────────────────┘
                 │
┌────────────────▼────────────────────────────────────────┐
│              Agent Orchestrator                          │
│  (Semantic Kernel + Multi-Agent Coordination)           │
├──────┬────────┬────────┬────────┬────────────────────────┤
│ Rec  │ Onboard│ Perf   │ Leave  │ ... More Agents        │
│ Agent│ Agent  │ Agent  │ Agent  │                        │
└──────┴────────┴────────┴────────┴────────────────────────┘
                 │
┌────────────────▼────────────────────────────────────────┐
│            Integration Layer                             │
├────────────────────────┬────────────────────────────────┤
│ Microsoft Graph API    │ Vector DB (RAG)                │
│ Azure AI Services      │ Database (SQLAlchemy)          │
│ External HR Systems    │ Document Storage               │
└────────────────────────┴────────────────────────────────┘
```

## 📁 Project Structure

```
hr-agent-system/
│
├── src/
│   ├── agents/                    # Agent implementations
│   │   ├── __init__.py
│   │   ├── base_agent.py         # Base agent class
│   │   ├── recruitment_agent.py  # Recruitment automation
│   │   ├── onboarding_agent.py   # Onboarding workflows
│   │   ├── performance_agent.py  # Performance management
│   │   └── leave_agent.py        # Leave management
│   │
│   ├── orchestrator/              # Agent orchestration
│   │   ├── __init__.py
│   │   ├── coordinator.py        # Multi-agent coordination
│   │   └── workflow_engine.py    # Workflow management
│   │
│   ├── integrations/              # External integrations
│   │   ├── __init__.py
│   │   ├── microsoft_graph.py    # Graph API client
│   │   ├── teams_bot.py          # Teams bot implementation
│   │   ├── azure_ai.py           # Azure AI services
│   │   └── hr_system.py          # HR system connectors
│   │
│   ├── models/                    # Data models
│   │   ├── __init__.py
│   │   ├── employee.py
│   │   ├── job.py
│   │   ├── leave_request.py
│   │   └── performance_review.py
│   │
│   ├── database/                  # Database layer
│   │   ├── __init__.py
│   │   ├── connection.py
│   │   └── repositories/
│   │
│   ├── rag/                       # RAG implementation
│   │   ├── __init__.py
│   │   ├── vector_store.py       # Vector database
│   │   ├── embeddings.py         # Embedding generation
│   │   └── retriever.py          # Document retrieval
│   │
│   ├── api/                       # FastAPI endpoints
│   │   ├── __init__.py
│   │   ├── routes/
│   │   │   ├── agents.py
│   │   │   ├── employees.py
│   │   │   └── webhooks.py
│   │   └── middleware/
│   │
│   ├── config/                    # Configuration
│   │   ├── __init__.py
│   │   ├── settings.py           # App settings
│   │   └── logging_config.py     # Logging setup
│   │
│   └── utils/                     # Utility functions
│       ├── __init__.py
│       ├── auth.py               # Authentication
│       └── helpers.py
│
├── teams_app/                     # Teams app manifest
│   ├── manifest.json
│   ├── color.png
│   └── outline.png
│
├── tests/                         # Test suite
│   ├── unit/
│   ├── integration/
│   └── e2e/
│
├── docs/                          # Documentation
│   ├── architecture.md
│   ├── api_reference.md
│   └── deployment.md
│
├── scripts/                       # Utility scripts
│   ├── setup_db.py
│   └── seed_data.py
│
├── .env.example                   # Environment variables template
├── requirements.txt               # Python dependencies
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## 🚀 Installation

### Prerequisites

- Python 3.10+
- Azure subscription
- Microsoft 365 tenant
- Teams admin access (for bot deployment)

### Setup

1. **Clone the repository**

```bash
git clone https://github.com/MinhAn15/hr-agent-system.git
cd hr-agent-system
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment**

```bash
cp .env.example .env
# Edit .env with your credentials
```

5. **Initialize database**

```bash
python scripts/setup_db.py
```

6. **Run the application**

```bash
uvicorn src.api.main:app --reload
```

## ⚙️ Configuration

### Azure AD App Registration

1. Register an app in Azure AD
2. Add Microsoft Graph API permissions:
   - `User.Read.All`
   - `Calendars.ReadWrite`
   - `Mail.Send`
   - `Files.ReadWrite.All`
3. Create client secret
4. Update `.env` with credentials

### Teams Bot Setup

1. Create bot in Azure Bot Service
2. Configure messaging endpoint
3. Add to Teams App Studio
4. Upload manifest from `teams_app/`

### OpenAI/Azure OpenAI

Configure either OpenAI or Azure OpenAI:

```env
# OpenAI
OPENAI_API_KEY=your_key

# OR Azure OpenAI
AZURE_OPENAI_ENDPOINT=your_endpoint
AZURE_OPENAI_API_KEY=your_key
```

## 📖 Usage

### Teams Bot Commands

Interact with agents via Teams:

```
@HRAgent help
@HRAgent find candidates for software engineer
@HRAgent schedule interview with John Doe
@HRAgent request leave from 2025-01-15 to 2025-01-20
@HRAgent check my performance goals
```

### REST API

```bash
# Create job posting
curl -X POST http://localhost:8000/api/jobs \
  -H "Content-Type: application/json" \
  -d '{"title": "Senior Engineer", "description": "..."}'

# Query agent
curl -X POST http://localhost:8000/api/agents/query \
  -H "Content-Type: application/json" \
  -d '{"message": "Find candidates", "agent": "recruitment"}'
```

### Python SDK

```python
from src.agents import RecruitmentAgent
from src.orchestrator import AgentCoordinator

# Initialize coordinator
coordinator = AgentCoordinator()

# Get recruitment agent
rec_agent = coordinator.get_agent("recruitment")

# Execute query
response = await rec_agent.process(
    "Find candidates with Python and Azure experience"
)
```

## 🤖 Agents

### Recruitment Agent

**Capabilities:**
- Job posting creation and management
- Resume parsing and candidate screening
- Interview scheduling via Microsoft Graph
- Email communication automation

### Onboarding Agent

**Capabilities:**
- New hire workflow automation
- Document generation and management
- Task assignment and tracking
- Equipment provisioning coordination

### Performance Agent

**Capabilities:**
- Goal setting and tracking
- Performance review scheduling
- Feedback collection and analysis
- Development plan creation

### Leave Management Agent

**Capabilities:**
- Leave request processing
- Approval workflow automation
- Balance calculation and tracking
- Calendar integration

## 🔌 Teams Integration

### Adaptive Cards

Rich interactive cards for user engagement:

```python
from botbuilder.schema import Attachment
from src.integrations.teams_bot import create_adaptive_card

card = create_adaptive_card(
    title="Interview Scheduled",
    body="Your interview with John Doe is confirmed",
    actions=[{"type": "Action.OpenUrl", "title": "Join Meeting"}]
)
```

### Proactive Messaging

Send notifications to users:

```python
await teams_bot.send_proactive_message(
    user_id="user@company.com",
    message="Your leave request has been approved"
)
```

## 📚 API Documentation

Full API documentation available at:

```
http://localhost:8000/docs  # Swagger UI
http://localhost:8000/redoc  # ReDoc
```

## 🛠️ Development

### Run Tests

```bash
pytest tests/
pytest tests/ --cov=src  # With coverage
```

### Code Quality

```bash
# Linting
flake8 src/

# Type checking
mypy src/

# Formatting
black src/
```

### Docker

```bash
# Build image
docker build -t hr-agent-system .

# Run container
docker-compose up
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Microsoft 365 Agent SDK Team
- LangChain Community
- Semantic Kernel Contributors

## 📞 Contact

For questions or support, please open an issue or contact the maintainers.

---

**Built with ❤️ using Microsoft 365 Agent Toolkit**
