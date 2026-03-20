#!/usr/bin/env python3
"""Fix encoding in oaissync_run.py"""
import sys
sys.path.insert(0, '.')

with open('v/script/oaissync_run.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if already added
if 'reconfigure' not in content:
    # Add after 'from pathlib import Path'
    insert_code = '''
# Windows 콘솔 UTF-8 인코딩 설정
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if sys.stderr and hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
'''
    content = content.replace(
        'from pathlib import Path\n\n# ==',
        'from pathlib import Path\n' + insert_code + '\n# =='
    )
    with open('v/script/oaissync_run.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print('UTF-8 encoding configuration added')
else:
    print('Already configured')
