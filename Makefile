.PHONY: fmt fix ci

fmt:
	uv run ruff format
	uv run ruff check --select I --fix --unsafe-fixes
	bun run -i oxfmt

fix:
	make fmt

ci:
	uv run ruff format --check
	uv run ruff check
	bun run -i oxfmt --check