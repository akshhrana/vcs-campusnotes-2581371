#!/usr/bin/env python3
"""CampusNotes - a small note keeper for VCS Assignment 2.

Student: Aksh Rana
URN: 2581371
Course: Version Control System (CSE25303), Assignment 2
"""
import sys

NOTES = [
    "Revise remote repository workflow",
    "Practise feature branches and pull requests",
    "Study Git hooks and release tags",
    "Prepare for the VCS viva",
]

def show_notes(notes):
    print("CampusNotes - Aksh Rana (URN 2581371)")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")

def search_notes(notes, keyword):
    found = [n for n in notes if keyword.lower() in n.lower()]
    if not found:
        print(f"No notes matching '{keyword}'.")
        return
    print(f"Matches for '{keyword}':")
    show_notes(found)

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "search":
        search_notes(NOTES, sys.argv[2])
    else:
        show_notes(NOTES)
