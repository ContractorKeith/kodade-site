# KödLocal

KödLocal runs a local model inside ködade. The bundled `kodade-modeld` daemon
stays on loopback and exposes a plain OpenAI-compatible endpoint at
`http://127.0.0.1:4470/v1`.

> **Pre-release status**
>
> There is no public download. Current macOS builds are unsigned test builds,
> and Windows human QA remains pending. See [platform and release
> status](../support/platform-status.md).

## Run a model on your machine

On macOS, KödLocal runs GGUF models through llama.cpp with Metal support. It
also supports MLX models through your own `mlx-lm` Python package; ködade does
not install Python packages for you.

The Windows build path has Vulkan and CPU-only variants. It does not include
CUDA, a CUDA toolkit, or cuDNN redistribution.

The daemon accepts local clients only. It is not a public model server.

## Use the free local-model tools

The free tier includes a desktop model manager and `kodade-local` for local
chat. The manager can download curated models with checksum verification, add
your own model files, load or unload a model, and report memory information.

Raw generation is also available through the loopback OpenAI-compatible Chat
Completions endpoint. That endpoint is useful for plain local generation. It is
not a drop-in primary-model endpoint for every agent CLI protocol.

## Add a bounded local agent with Pro

Pro adds the agent layer around the local model:

- an agent loop with confined project tools
- KödMem project context and checkpoints
- harness instructions and skills in the agent context
- a `delegate` MCP server so Claude Code or Codex can hand a bounded subtask to
  the local model
- saved remote backends, with a per-session picker

The local agent's tools are confined to the selected project and use explicit
validation. A local model does not receive an unrestricted shell. Delegated
work has fixed tool and output budgets so the calling agent remains in control.

## Choose remote backends deliberately

The implicit **This Mac** backend is local. Pro can save a remote HTTP(S)
endpoint and select it for one KödLocal session. Before a non-local launch,
ködade warns that prompts, project context, KödMem context, and enabled agent
requests will be sent to that endpoint. Use a backend whose operator and
privacy policy you trust.

## Set realistic expectations

Small local models are useful workers for bounded tasks, summarization, and
private context. They are not frontier-model replacements. Tool-calling
reliability varies by model, so a model that is fine for chat may not be a good
choice for an agent loop.

Model files, downloads, the daemon lifecycle, and model management are
desktop-only in version 1. They are not available from KödWeb browser sessions.
See [KödWeb](kodweb.md), [KödMCP](kodmcp.md), and [local data and
privacy](../trust/local-data-privacy.md) for the related local-data boundaries.
