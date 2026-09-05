#!/usr/bin/env bash
# SPDX-FileCopyrightText: Johannes Keyser <johannes.keyser@uni-hamburg.de>
# SPDX-License-Identifier: EUPL-1.2
#
# Purpose: create a git tag for a release from the project version file.
# See the release notes in docs/README.md for the full workflow.
#
# This script helps keep the tag name and the version file in sync.
# It expects VERSION to contain a semver-like value such as 0.1.0.

set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PROJECT_DIR="$SCRIPT_DIR"
VERSION_FILE="$PROJECT_DIR/VERSION"

if [[ ! -f "$VERSION_FILE" ]]; then
  echo "ERROR: VERSION file not found at $VERSION_FILE" >&2
  exit 1
fi

VERSION=$(tr -d '\r\n' < "$VERSION_FILE")

if [[ ! "$VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "ERROR: VERSION must use SemVer format, e.g. 0.1.0" >&2
  exit 1
fi

TAG="v${VERSION}"

if git rev-parse --verify --quiet "$TAG" >/dev/null; then
  echo "ERROR: Tag $TAG already exists." >&2
  exit 1
fi

git tag "$TAG"
echo "Created tag: $TAG"
echo "Ready for git push, then CI creates the release artifacts."
