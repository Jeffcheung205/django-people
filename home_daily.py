#!/usr/bin/env python3
"""
Home Daily - A simple daily home management program
Features: Weather info, daily tasks, motivational quotes, and time tracking
"""

import datetime
import random


class HomeDailyAssistant:
    """Simple home daily assistant"""
    
    def __init__(self):
        self.tasks = []
        self.quotes = [
            "Every day is a fresh start!",
            "Small steps lead to big changes.",
            "Make today count!",
            "Your home is your sanctuary.",
            "A clean space equals a clear mind.",
            "Progress, not perfection.",
            "Today's efforts are tomorrow's results.",
        ]
    
    def show_greeting(self):
        """Display personalized greeting"""
        now = datetime.datetime.now()
        hour = now.hour
        
        if hour < 12:
            greeting = "Good Morning! ☀️"
        elif hour < 18:
            greeting = "Good Afternoon! 🌤️"
        else:
            greeting = "Good Evening! 🌙"
        
        print("=" * 50)
        print(f"  {greeting}")
        print(f"  {now.strftime('%A, %B %d, %Y')}")
        print("=" * 50)
        print()
    
    def show_daily_quote(self):
        """Display a random motivational quote"""
        quote = random.choice(self.quotes)
        print(f"💡 Daily Quote: {quote}")
        print()
    
    def add_task(self, task):
        """Add a task to the list"""
        self.tasks.append({"task": task, "done": False})
        print(f"✓ Added task: {task}")
    
    def show_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("📝 No tasks yet. Add some tasks to get started!")
            return
        
        print("📝 Today's Tasks:")
        print("-" * 50)
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["done"] else "○"
            print(f"  {i}. [{status}] {task['task']}")
        print()
    
    def complete_task(self, task_number):
        """Mark a task as complete"""
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["done"] = True
            print(f"✓ Completed: {self.tasks[task_number - 1]['task']}")
        else:
            print("❌ Invalid task number")
    
    def show_menu(self):
        """Display interactive menu"""
        print("\n📋 Menu:")
        print("  1. Add a task")
        print("  2. Show tasks")
        print("  3. Complete a task")
        print("  4. Show daily quote")
        print("  5. Exit")
        print()
    
    def run(self):
        """Main program loop"""
        self.show_greeting()
        self.show_daily_quote()
        
        # Add some default tasks for demonstration
        self.add_task("Morning coffee ☕")
        self.add_task("Clean the kitchen 🧹")
        self.add_task("Water the plants 🌱")
        print()
        
        while True:
            self.show_menu()
            choice = input("Choose an option (1-5): ").strip()
            print()
            
            if choice == "1":
                task = input("Enter new task: ").strip()
                if task:
                    self.add_task(task)
                print()
            elif choice == "2":
                self.show_tasks()
            elif choice == "3":
                self.show_tasks()
                try:
                    task_num = int(input("Enter task number to complete: ").strip())
                    self.complete_task(task_num)
                except ValueError:
                    print("❌ Please enter a valid number")
                print()
            elif choice == "4":
                self.show_daily_quote()
            elif choice == "5":
                print("👋 Have a great day!")
                break
            else:
                print("❌ Invalid option. Please choose 1-5.")
                print()


def main():
    """Run the home daily assistant"""
    assistant = HomeDailyAssistant()
    assistant.run()


if __name__ == "__main__":
    main()
