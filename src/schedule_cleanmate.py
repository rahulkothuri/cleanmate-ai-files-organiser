#!/usr/bin/env python3
"""
Helper script to schedule CleanMate runs using cron
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

def setup_cron_job(frequency, time=None):
    """
    Set up a cron job to run CleanMate at specified frequency
    
    Parameters:
    frequency (str): 'daily', 'weekly', or 'monthly'
    time (str): Time in 24-hour format (HH:MM)
    """
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cleanmate.py")
    
    # Make sure the script is executable
    os.chmod(script_path, 0o755)
    
    # Default time is 8 PM if not specified
    if not time:
        time = "20:00"
    
    hour, minute = time.split(":")
    
    # Create cron expression based on frequency
    if frequency == "daily":
        cron_expr = f"{minute} {hour} * * *"
    elif frequency == "weekly":
        cron_expr = f"{minute} {hour} * * 0"  # Sunday
    elif frequency == "monthly":
        cron_expr = f"{minute} {hour} 1 * *"  # 1st day of month
    else:
        print(f"Invalid frequency: {frequency}")
        sys.exit(1)
    
    # Full cron job line
    cron_job = f"{cron_expr} {script_path}"
    
    # Check existing crontab
    try:
        result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
        if result.returncode == 0:
            existing_crontab = result.stdout
        else:
            existing_crontab = ""
    except Exception:
        existing_crontab = ""
    
    # Check if job already exists
    if script_path in existing_crontab:
        print("CleanMate is already scheduled. Remove existing schedule first.")
        sys.exit(1)
    
    # Add new cron job
    new_crontab = existing_crontab.strip() + f"\n{cron_job}\n"
    
    # Write to temp file
    temp_file = "/tmp/cleanmate_crontab"
    with open(temp_file, "w") as f:
        f.write(new_crontab)
    
    # Install new crontab
    try:
        subprocess.run(["crontab", temp_file], check=True)
        os.remove(temp_file)
        print(f"CleanMate scheduled to run {frequency} at {time}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to schedule CleanMate: {e}")
        sys.exit(1)

def remove_cron_job():
    """Remove CleanMate from crontab"""
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cleanmate.py")
    
    # Check existing crontab
    try:
        result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
        if result.returncode == 0:
            existing_crontab = result.stdout
        else:
            print("No crontab found.")
            return
    except Exception:
        print("Failed to read crontab.")
        return
    
    # Filter out CleanMate jobs
    new_crontab = "\n".join([line for line in existing_crontab.split("\n") 
                            if script_path not in line])
    
    # Write to temp file
    temp_file = "/tmp/cleanmate_crontab"
    with open(temp_file, "w") as f:
        f.write(new_crontab)
    
    # Install new crontab
    try:
        subprocess.run(["crontab", temp_file], check=True)
        os.remove(temp_file)
        print("CleanMate schedule removed.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to update crontab: {e}")

def main():
    parser = argparse.ArgumentParser(description="Schedule CleanMate to run automatically")
    
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add a scheduled run")
    add_parser.add_argument("frequency", choices=["daily", "weekly", "monthly"], 
                          help="How often to run CleanMate")
    add_parser.add_argument("--time", help="Time to run (24-hour format, e.g. 20:00)", 
                          default="20:00")
    
    # Remove command
    remove_parser = subparsers.add_parser("remove", help="Remove scheduled runs")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List scheduled runs")
    
    args = parser.parse_args()
    
    if args.command == "add":
        setup_cron_job(args.frequency, args.time)
    elif args.command == "remove":
        remove_cron_job()
    elif args.command == "list":
        try:
            result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
            if result.returncode == 0:
                script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cleanmate.py")
                cron_jobs = [line for line in result.stdout.split("\n") if script_path in line]
                
                if cron_jobs:
                    print("Scheduled CleanMate runs:")
                    for job in cron_jobs:
                        print(f"  {job}")
                else:
                    print("No scheduled CleanMate runs found.")
            else:
                print("No crontab found.")
        except Exception as e:
            print(f"Failed to list scheduled runs: {e}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
