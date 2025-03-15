```markdown
# LinkedIn Content Automation Toolkit

A multi-agent system that analyzes RSS feed articles, generates LinkedIn posts, and provides post optimization feedback. Built with Python, OpenAI, and Streamlit.

## Features

- **RSS Feed Processing**: Fetches and parses latest AI articles from TechCrunch
- **HTML Content Extraction**: Cleans and extracts raw text from web articles
- **LinkedIn Post Generation**: Creates viral-style posts using proven templates
- **Post Analysis**: Provides detailed feedback and optimization suggestions
- **Streamlit Dashboard**: Displays results in interactive HTML tables

## Installation

1. Clone repository:
```bash
git clone [your-repo-url]
cd linkedin-content-automation
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file:
```env
OPENAI_API_KEY=your_openai_key
AGENTOPS_API_KEY=your_agentops_key
```

## Usage

1. Start Streamlit app:
```bash
streamlit run final_linkedin_agent.py
```

2. The system will:
   - Fetch 3 latest articles from TechCrunch AI RSS feed
   - Generate LinkedIn posts for each article
   - Create optimization reports
   - Display results in a web dashboard

## Configuration

Modify these elements for customization:

1. **RSS Feed**: Edit `rss_url` in `rss_script.py`
2. **Post Templates**: Modify prompts in `prompts.py`
3. **Output Formatting**: Adjust `generate_html_table()` in `final_linkedin_agent.py`

## Project Structure

```
├── final_linkedin_agent.py    # Main application logic
├── prompts.py                 # AI prompt templates
├── rss_script.py              # RSS feed processor
├── requirements.txt           # Dependencies
└── .env                       # API credentials
```

## Agents

1. **HTML Parser**: Extracts clean text from web pages
2. **Post Generator**: Creates LinkedIn content using viral templates
3. **Post Analyst**: Provides optimization feedback with ratings

## Dependencies

- **Core**: Python 3.9+
- **AI**: OpenAI, AgentOps
- **Web**: Requests, BeautifulSoup4
- **UI**: Streamlit
- **Processing**: lxml, html5lib

## License

MIT License - See [LICENSE](LICENSE) for details

---

**Note**: Requires valid API keys from [OpenAI](https://platform.openai.com/) and [AgentOps](https://www.agentops.ai/). Replace the default TechCrunch RSS feed URL in `rss_script.py` for different content sources.
```