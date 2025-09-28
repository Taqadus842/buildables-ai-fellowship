# Solution Architecture

## Components
1. **Data Ingestion** (PDF, DOCX, TXT) → preprocessing
2. **LlamaIndex** → Vector index built from documents
3. **LangChain Agent** → Adds tool integration
   - ClauseClassifierTool
   - Calculator
4. **Streamlit Frontend** → Simple UI

## Flow
User uploads → Index built → User asks query → Agent decides retrieval or tool → Returns summarized/classified answer.
