#!/usr/bin/env python3
"""
Script to merge CSV poster data with existing JSON files.
Creates new processed JSON files with: authors, openreview, title, abstract, number, category, is_spotlight
"""

import csv
import json
from pathlib import Path


def normalize_title(title: str) -> str:
    """Normalize title for matching by lowercasing, removing extra whitespace, and standardizing punctuation."""
    import re
    title = title.lower().strip()
    # Remove "title:" prefix if present
    if title.startswith('title:'):
        title = title[6:].strip()
    # Standardize dashes (en-dash, em-dash -> hyphen)
    title = title.replace('–', '-').replace('—', '-')
    # Normalize "state-space" vs "state space"
    title = title.replace('state-space', 'state space')
    # Normalize whitespace
    title = ' '.join(title.split())
    # Remove accidental category numbers like "Large 5 Reasoning" -> "Large Reasoning"
    # This handles cases where "5" got accidentally inserted
    title = re.sub(r'\s+\d+\s+', ' ', title)
    # Normalize British vs American spelling for common cases
    title = title.replace('behaviour', 'behavior')
    title = title.replace('generalisation', 'generalization')
    # Handle singular/plural variations at word boundaries
    title = re.sub(r'\bcontains\b', 'contain', title)
    title = re.sub(r'\bmodels\b', 'model', title)
    return title


def clean_title(title: str) -> str:
    """Clean up title from CSV (remove 'Title:' prefix, fix spacing issues)."""
    import re
    title = title.strip()
    # Remove "Title:" prefix if present
    if title.lower().startswith('title:'):
        title = title[6:].strip()
    # Remove accidental category numbers like "Large 5 Reasoning" -> "Large Reasoning"
    title = re.sub(r'\s+(\d+)\s+', ' ', title)
    # Also handle "Finetuned 5 Reasoning" pattern
    title = re.sub(r'(\w)\s+\d+\s+(\w)', r'\1 \2', title)
    return title


def load_csv_data(csv_path: Path) -> list[dict]:
    """Load poster data from CSV file."""
    entries = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Clean up category - remove the leading number
            category = row['Category (final)'].strip()
            if category and category[0].isdigit():
                # Remove "1 " prefix from "1 Circuits and Reverse Engineering"
                parts = category.split(' ', 1)
                if len(parts) > 1:
                    category = parts[1]
            
            entry = {
                'number': int(row['Room Location']),
                'title': clean_title(row['Title']),
                'abstract': row['Abstract'].strip(),
                'category': category,
                'is_spotlight': 'Spotlight' in row['Status'],
                'authors': None,  # Will be filled from JSON
                'openreview': None,  # Will be filled from JSON
            }
            entries.append(entry)
    return entries


def load_json_data(json_paths: list[Path]) -> dict[str, dict]:
    """Load existing JSON files and create a lookup by normalized title."""
    title_lookup = {}
    for json_path in json_paths:
        if not json_path.exists():
            print(f"Warning: {json_path} does not exist")
            continue
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                norm_title = normalize_title(item['title'])
                title_lookup[norm_title] = {
                    'authors': item['authors'],
                    'openreview': item['openreview'],
                    'original_title': item['title']
                }
    return title_lookup


def merge_data(csv_entries: list[dict], json_lookup: dict[str, dict]) -> tuple[list[dict], list[str], list[str]]:
    """
    Merge CSV data with JSON data by matching titles.
    Returns: (merged_entries, csv_only_titles, json_only_titles)
    """
    merged = []
    csv_only = []
    matched_json_titles = set()
    
    for entry in csv_entries:
        norm_title = normalize_title(entry['title'])
        if norm_title in json_lookup:
            json_data = json_lookup[norm_title]
            entry['authors'] = json_data['authors']
            entry['openreview'] = json_data['openreview']
            matched_json_titles.add(norm_title)
        else:
            csv_only.append(entry['title'])
        merged.append(entry)
    
    # Find JSON entries that weren't in CSV
    json_only = [
        json_lookup[norm_title]['original_title'] 
        for norm_title in json_lookup 
        if norm_title not in matched_json_titles
    ]
    
    return merged, csv_only, json_only


def main():
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / 'data'
    raw_data_dir = base_dir / 'raw-data'
    
    # Process morning/early data
    print("=" * 60)
    print("Processing MORNING/EARLY poster data...")
    print("=" * 60)
    
    morning_csv = load_csv_data(raw_data_dir / 'morning_poster_data.csv')
    early_json_lookup = load_json_data([
        data_dir / 'early_poster.json',
        data_dir / 'early_spotlight.json'
    ])
    
    early_merged, early_csv_only, early_json_only = merge_data(morning_csv, early_json_lookup)
    
    if early_csv_only:
        print(f"\n⚠️  {len(early_csv_only)} entries in MORNING CSV but NOT in early JSON files:")
        for title in early_csv_only:
            print(f"  - {title}")
    
    if early_json_only:
        print(f"\n⚠️  {len(early_json_only)} entries in early JSON but NOT in MORNING CSV:")
        for title in early_json_only:
            print(f"  - {title}")
    
    if not early_csv_only and not early_json_only:
        print("✅ All entries matched perfectly!")
    
    # Save early processed data
    output_path = data_dir / 'early_poster_processed.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(early_merged, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Saved {len(early_merged)} entries to {output_path}")
    
    # Process afternoon/late data
    print("\n" + "=" * 60)
    print("Processing AFTERNOON/LATE poster data...")
    print("=" * 60)
    
    afternoon_csv = load_csv_data(raw_data_dir / 'afternoon_poster_data.csv')
    late_json_lookup = load_json_data([
        data_dir / 'late_poster.json',
        data_dir / 'late_spotlight.json'
    ])
    
    late_merged, late_csv_only, late_json_only = merge_data(afternoon_csv, late_json_lookup)
    
    if late_csv_only:
        print(f"\n⚠️  {len(late_csv_only)} entries in AFTERNOON CSV but NOT in late JSON files:")
        for title in late_csv_only:
            print(f"  - {title}")
    
    if late_json_only:
        print(f"\n⚠️  {len(late_json_only)} entries in late JSON but NOT in AFTERNOON CSV:")
        for title in late_json_only:
            print(f"  - {title}")
    
    if not late_csv_only and not late_json_only:
        print("✅ All entries matched perfectly!")
    
    # Save late processed data
    output_path = data_dir / 'afternoon_poster_processed.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(late_merged, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Saved {len(late_merged)} entries to {output_path}")
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    early_spotlights = sum(1 for e in early_merged if e['is_spotlight'])
    late_spotlights = sum(1 for e in late_merged if e['is_spotlight'])
    print(f"Morning/Early: {len(early_merged)} total ({early_spotlights} spotlights)")
    print(f"Afternoon/Late: {len(late_merged)} total ({late_spotlights} spotlights)")


if __name__ == '__main__':
    main()

