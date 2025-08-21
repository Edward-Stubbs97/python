import sqlite3

def add_task(task, due_Date, status, quit):

    conn = sqlite3.connect("to_do_list.db")

    cursor = conn.cursor()

    cursor.execute(
        "INSERT OR REPLACE INTO to_do_list (task, due_date, status) VALUES (?, ?, ?)",
        (task, due_Date, status)
    )

    conn.commit()
    conn.close()

    print(f"{task} has been added to, to do list")


def task_status(task):

    conn = sqlite3.connect("to_do_list.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT task, due_date, status FROM to_do_list WHERE task = ?",
        (task,)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        task, due_date, status = result
        print(f"{task}: {due_date}: {status}")
    else:
        print(f"there is no result for {task} in the database")


def update_remove_task():
    action = input("Do you want to update or delete a task? ").lower()

    if action not in ["delete", "update"]:
        print("Invalid action. Please type 'update' or 'delete'.")
        return

    task = input("Which task do you want to modify? ").lower()

    conn = sqlite3.connect("to_do_list.db")
    cursor = conn.cursor()

    if action == "delete":
        cursor.execute("DELETE FROM to_do_list WHERE task = ?", (task,))
        conn.commit()
        print(f"{task} has been deleted from your to-do list.")

    elif action == "update":
        new_due_date = input("Enter the new due date: ")
        new_status = input("Enter the new status: ")
        cursor.execute(
            "UPDATE to_do_list SET due_date = ?, status = ? WHERE task = ?",
            (new_due_date, new_status, task)
        )
        conn.commit()
        print(f"{task} has been updated.")

    conn.close()


action = input("Do you want to add, view, update, delete or quit a task? ").lower()

if action == "add":
    task = input("Enter task name: ")
    due_date = input("Enter due date: ")
    status = input("Enter status: ")
    add_task(task, due_date, status)

elif action == "view":
    task = input("Which task do you want to see? ")
    task_status(task)

elif action == "quit":
    print("Goodbye")

elif action in ["update", "delete"]:
    update_remove_task()

else:
    print("Invalid action.")

