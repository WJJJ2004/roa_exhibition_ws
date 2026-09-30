#!/usr/bin/env bash

workspace_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

source /opt/ros/humble/setup.bash
if [[ ! -f "${workspace_dir}/install/setup.bash" ]]; then
  echo "ERROR: workspace is not built. Run ./build_exhibition.sh first." >&2
  return 1 2>/dev/null || exit 1
fi
source "${workspace_dir}/install/setup.bash"
