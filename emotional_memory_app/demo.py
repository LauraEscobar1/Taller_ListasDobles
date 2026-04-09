from doubly_linked_list import DoublyLinkedList

def run_demo():
    memory_list = DoublyLinkedList()

    memory_list.insert_at_end("2023-01-10", "First day at university", "anxious")
    memory_list.insert_at_end("2023-05-20", "Passed all exams", "happy")
    memory_list.insert_at_end("2023-08-15", "Trip with friends", "excited")

    print("\nForward traversal:")
    for m in memory_list.traverse_forward():
        print(m)

    print("\nBackward traversal:")
    for m in memory_list.traverse_backward():
        print(m)

    print("\nSearching for 'happy':")
    for m in memory_list.search_by_emotion("happy"):
        print(m)


if __name__ == "__main__":
    run_demo()