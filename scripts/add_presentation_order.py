#!/usr/bin/env python3
"""
Script to add presentation_order to spotlight entries in processed JSON files
based on the spotlight_ordering.csv file.
"""

import csv
import json
from pathlib import Path


def normalize_title(title: str) -> str:
    """Normalize title for matching."""
    title = title.lower().strip()
    # Standardize dashes
    title = title.replace('–', '-').replace('—', '-')
    # Normalize whitespace
    title = ' '.join(title.split())
    return title


def load_csv_ordering(csv_path: Path) -> dict:
    """
    Load spotlight ordering from CSV.
    Returns dict mapping (session, normalized_title) -> presentation_order
    """
    ordering = {
        'morning': {},
        'afternoon': {}
    }
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            slot = row['ASSIGNED SLOT'].strip().lower()
            if slot not in ('morning', 'afternoon'):
                continue  # Skip N/A entries
            
            order = row['Presentation order'].strip()
            if not order:
                continue
            
            title = row['What is the title of your paper?'].strip()
            if not title:
                continue
                
            norm_title = normalize_title(title)
            ordering[slot][norm_title] = int(order)
    
    return ordering


def update_json_with_ordering(json_path: Path, ordering: dict, session: str) -> tuple[int, int]:
    """
    Update JSON file with presentation_order field for spotlights.
    Returns (updated_count, total_spotlights)
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    updated = 0
    total_spotlights = 0
    
    for entry in data:
        if not entry.get('is_spotlight'):
            continue
        
        total_spotlights += 1
        norm_title = normalize_title(entry['title'])
        
        if norm_title in ordering[session]:
            entry['presentation_order'] = ordering[session][norm_title]
            updated += 1
            print(f"  ✓ Order {entry['presentation_order']:2d}: {entry['title'][:60]}...")
        else:
            # Try fuzzy matching for titles that might differ slightly
            matched = False
            for csv_title, order in ordering[session].items():
                # Check if one contains the other (for partial matches)
                if csv_title in norm_title or norm_title in csv_title:
                    entry['presentation_order'] = order
                    updated += 1
                    matched = True
                    print(f"  ✓ Order {entry['presentation_order']:2d} (fuzzy): {entry['title'][:50]}...")
                    break
            
            if not matched:
                print(f"  ✗ No match found: {entry['title'][:60]}...")
    
    # Sort by presentation_order for spotlights that have it
    # This doesn't change the file order, just adds the field
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    return updated, total_spotlights


def main():
    base_dir = Path(__file__).parent.parent
    csv_path = base_dir / 'spotlight_ordering.csv'
    data_dir = base_dir / 'data'
    
    print("Loading spotlight ordering from CSV...")
    ordering = load_csv_ordering(csv_path)
    print(f"  Found {len(ordering['morning'])} morning spotlights")
    print(f"  Found {len(ordering['afternoon'])} afternoon spotlights")
    
    print("\n" + "=" * 60)
    print("Updating MORNING (early_poster_processed.json)...")
    print("=" * 60)
    updated, total = update_json_with_ordering(
        data_dir / 'early_poster_processed.json',
        ordering,
        'morning'
    )
    print(f"\n✅ Updated {updated}/{total} morning spotlights")
    
    print("\n" + "=" * 60)
    print("Updating AFTERNOON (afternoon_poster_processed.json)...")
    print("=" * 60)
    updated, total = update_json_with_ordering(
        data_dir / 'afternoon_poster_processed.json',
        ordering,
        'afternoon'
    )
    print(f"\n✅ Updated {updated}/{total} afternoon spotlights")
    
    print("\n" + "=" * 60)
    print("DONE! Now update layouts/spotlights/list.html to sort by presentation_order")
    print("=" * 60)


if __name__ == '__main__':
    main()

