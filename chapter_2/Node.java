class Node {
	Node next = null;
	int data;

	public Node(int d) {
		data = d;
	}

	public static void main(String[] args) {
		System.out.println("Hello World");
	}

	void appendToTail(int d) {
		Node end = new Node(d);
		Node n = this;
		while (n!= null) {
			n = n.next;
		}
		n.next = end;
	}
}
