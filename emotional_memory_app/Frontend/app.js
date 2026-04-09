class Node {
  constructor(date, description, emotion) {
    this.date = date;
    this.description = description;
    this.emotion = emotion;
    this.next = null;
    this.prev = null;
  }
}

class DoublyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.current = null;
    this.size = 0;
  }

  insertEnd(date, desc, emo) {
    const node = new Node(date, desc, emo);

    if (!this.head) {
      this.head = this.tail = this.current = node;
    } else {
      node.prev = this.tail;
      this.tail.next = node;
      this.tail = node;
    }

    this.size++;
  }

  next() {
    if (this.current && this.current.next) {
      this.current = this.current.next;
    }
  }

  prev() {
    if (this.current && this.current.prev) {
      this.current = this.current.prev;
    }
  }

  deleteCurrent() {
    if (!this.current) return;

    const node = this.current;

    if (node.prev) node.prev.next = node.next;
    else this.head = node.next;

    if (node.next) node.next.prev = node.prev;
    else this.tail = node.prev;

    this.current = node.next || node.prev;
    this.size--;
  }
}

const list = new DoublyLinkedList();

function addMemory() {
  const date = document.getElementById('inputDate').value;
  const desc = document.getElementById('inputDesc').value;
  const emo = document.getElementById('inputEmotion').value;

  if (!date || desc.length < 3 || !emo) return;

  list.insertEnd(date, desc, emo);
  render();
}

function navigate(dir) {
  if (dir === 'next') list.next();
  else list.prev();
  render();
}

function deleteMemory() {
  list.deleteCurrent();
  render();
}

function render() {
  document.getElementById('count-total').textContent = list.size;

  if (!list.current) {
    document.getElementById('emptyState').style.display = 'block';
    document.getElementById('memoryContent').style.display = 'none';
    return;
  }

  document.getElementById('emptyState').style.display = 'none';
  document.getElementById('memoryContent').style.display = 'block';

  document.getElementById('mvEmotionName').textContent = list.current.emotion;
  document.getElementById('mvDate').textContent = list.current.date;
  document.getElementById('mvDescription').textContent = list.current.description;
}