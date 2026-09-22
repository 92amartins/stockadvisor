run:
	@uv run python src/stockadvisor/agent.py

dev:
	@uv run langgraph dev --config src/stockadvisor/langgraph.json