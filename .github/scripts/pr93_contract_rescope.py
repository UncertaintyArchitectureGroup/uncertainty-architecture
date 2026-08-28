import json
from pathlib import Path

path = Path('.github/policy/repository-contract-change-coupling.json')
data = json.loads(path.read_text())

updates = {
    '.github/workflows/export-platform-renditions.yml': [
        'name: Export platform renditions',
        'workflow_dispatch:',
        'npm run publication:bundle',
        'thinking-systems-platform-renditions',
        'fetch-depth: 0',
        'dist/publication/thinking-systems/figures/png/**',
        'dist/publication/thinking-systems/renditions/**',
        'UA_PDF_REPOSITORY_REF: ${{ github.event.pull_request.head.sha || github.sha }}',
        'npm run publication:verify-package',
        'quartz/scripts/verify-publication-package.test.mjs',
    ],
    'quartz/scripts/render-copy-ready.mjs': [
        'embedLocalImages',
        'replaceMediumImagesWithRemoteSources',
        'immutable-raw-github-url',
        'data:image/png;base64',
        'copy-ready.html',
        'manual-select-all-copy',
        'javascript_copy_controls: false',
    ],
    'quartz/scripts/verify-publication-package.mjs': [
        'assertPlatformFigureInventory',
        'remoteGithubImageSources',
        'publication_state === "candidate"',
        'publication_ready === false',
        'Figure 8A and 8B must travel together',
        'Medium copy-ready must not use data-URI images',
        'copy-ready HTML contains obsolete copy controls',
    ],
    'quartz/scripts/verify-publication-package.test.mjs': [
        'platform verifier requires nine figures with Figure 8A and 8B coupled',
        'platform verifier rejects incomplete Figure 8 coupling',
        'remote image inventory recognizes immutable GitHub image sources',
    ],
}

found = set()
for item in data.get('critical_files', []):
    p = item.get('path')
    if p in updates:
        item['required_text'] = updates[p]
        found.add(p)

missing = set(updates) - found
if missing:
    raise SystemExit(f'Missing critical file blocks: {sorted(missing)}')

path.write_text(json.dumps(data, indent=2) + '\n')
print('Repository contract rescaled to platform-only PR93 scope')
