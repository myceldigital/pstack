#!/usr/bin/env bash
set -euo pipefail

# pstack installer — installs skill files into Claude Code's skill directory

PSTACK_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_DIR="${HOME}/.claude/skills/pstack"

echo "╔══════════════════════════════════════════════════╗"
echo "║  pstack — Palantir Deployment Strategist AI Team ║"
echo "╚══════════════════════════════════════════════════╝"
echo ""

# Check for Claude Code skill directory
if [ ! -d "${HOME}/.claude" ]; then
  echo "Creating ~/.claude directory..."
  mkdir -p "${HOME}/.claude"
fi

if [ ! -d "${HOME}/.claude/skills" ]; then
  echo "Creating ~/.claude/skills directory..."
  mkdir -p "${HOME}/.claude/skills"
fi

# Create symlink or copy
if [ -L "$SKILL_DIR" ]; then
  echo "Removing existing pstack symlink..."
  rm "$SKILL_DIR"
fi

if [ -d "$SKILL_DIR" ]; then
  echo "Removing existing pstack installation..."
  rm -rf "$SKILL_DIR"
fi

echo "Installing pstack to ${SKILL_DIR}..."
ln -s "$PSTACK_DIR" "$SKILL_DIR"

echo ""
echo "✅ pstack installed successfully!"
echo ""
echo "Available skills:"
echo "  /bootcamp          — Start a new customer engagement"
echo "  /ontology-vision   — Strategic ontology design"
echo "  /ontology-architect — Lock ontology architecture"
echo "  /pipeline-plan     — Design data pipeline architecture"
echo "  /data-connector    — Configure data connections"
echo "  /pipeline-builder  — Build transformation pipelines"
echo "  /workshop-builder  — Build Workshop applications"
echo "  /aip-architect     — Design AIP agents"
echo "  /osdk-developer    — Build OSDK applications"
echo "  /slate-builder     — Build Slate applications"
echo "  /foundry-reviewer  — Structural audit"
echo "  /foundry-security  — Security audit"
echo "  /foundry-qa        — End-to-end testing"
echo "  /apollo-deployer   — Apollo deployment"
echo "  /training-writer   — Training materials"
echo "  /deployment-retro  — Retrospective"
echo "  /memory-curator    — Curate structured repo memory"
echo "  /skill-improver    — Draft bounded improvement proposals"
echo "  /careful           — Safety mode"
echo "  /freeze            — Scope restriction"
echo "  /guard             — Maximum safety (careful + freeze)"
echo ""
echo "Start with: /bootcamp"
