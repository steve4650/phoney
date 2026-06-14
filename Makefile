.PHONY: fmt

fmt:
	uv run ruff format
	uv run ruff check --unsafe-fixes
	bun run oxfmt
