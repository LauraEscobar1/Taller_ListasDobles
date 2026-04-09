from flask import Flask, request, jsonify
from doubly_linked_list import DoublyLinkedList

app = Flask(__name__)

memory_list = DoublyLinkedList()

@app.route("/add", methods=["POST"])
def add_memory():
    data = request.json

    memory_list.insert_at_end(
        data["date"],
        data["description"],
        data["emotion"]
    )

    return jsonify({"message": "Memory added"})


@app.route("/all", methods=["GET"])
def get_all():
    memories = []

    node = memory_list.head
    while node:
        memories.append({
            "date": node.date,
            "description": node.description,
            "emotion": node.emotion
        })
        node = node.next

    return jsonify(memories)


if __name__ == "__main__":
    app.run(debug=True)