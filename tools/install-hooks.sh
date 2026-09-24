#!/usr/bin/env bash
# Install a pre-commit hook that runs tools/check_public.py on staged files.
# Run once after cloning:  bash tools/install-hooks.sh
set -euo pipefail
root="$(git rev-parse --show-toplevel)"
hook="$root/.git/hooks/pre-commit"
cat > "$hook" <<'EOF'
#!/usr/bin/env bash
exec python3 "$(git rev-parse --show-toplevel)/tools/check_public.py" --staged
EOF
chmod +x "$hook"
echo "Installed $hook"
