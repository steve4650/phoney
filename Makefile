.PHONY: fmt

fmt:
	uv run ruff format
	uv run ruff check --select I --fix --unsafe-fixes
	bun run oxfmt
