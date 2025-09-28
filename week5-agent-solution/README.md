# Contract Analyzer Assistant - LLM Agent Solution

## Problem Statement
Law firms, startups, and freelancers waste hours reading contracts line by line to extract payment terms, termination clauses, and risk points. This project automates **contract summarization and clause classification** using LLMs with document retrieval.

## Solution Architecture
- **LlamaIndex** → Ingests contracts (PDF/DOCX/TXT) and builds a searchable vector index.
- **LangChain Agent** → Adds tools:
  - Calculator (numeric reasoning)
  - ClauseClassifierTool (classify obligations, payments, risks)
- **Streamlit UI** → Upload contracts, build index, query, and run tool-assisted analysis.

## Setup Instructions
1. Clone repo:
   ```bash
   git clone <your_repo_url>
   cd week5-agent-solution
   ```
2. Create environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Setup API key:
   ```bash
   cp .env.example .env
   # Add your OPENAI_API_KEY inside .env
   ```
5. (Optional) Add contracts into `data/` folder.
6. Build index:
   ```bash
   python src/llama_index_agent.py --build
   ```
7. Query contract:
   ```bash
   python src/llama_index_agent.py --query "What is the termination clause?"
   ```
8. Run UI:
   ```bash
   streamlit run src/main.py
   ```

## Usage Examples
- **Summarize contract** → “Summarize this contract in 5 sentences.”
- **Find payment terms** → “What is the payment term?”
- **Tool integration** → “If penalty is $500/day for 20 days, what’s total?”
- **Clause classification** → “Classify indemnity clause.”

## Technical Challenges
- Chunking long contracts
- Combining retrieval + agent reasoning
- Handling PDF/docx parsing errors
- Tool integration into LangChain agent

## Impact & Results
- Saves ~3–5 hours per contract
- Reduces manual review errors
- Enables small firms to scale reviews

## Future Improvements
- Risk scoring system
- Source-cited answers
- Integration with legal CRMs
- Multi-document comparison
