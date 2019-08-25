package chapter_2;

//  Author: Aaron Maritz
//	Partition -> partition a linked list around a  value x, such that all nodes less than x
//	Appear before all nodes greater than or equal to x

//  Could just iterate through the list, for all elements < x -> delete the node and append it to the front.
//	If not just go to the next node
public class QuestionFour {

	public Node Partition(Node head, int x) {
		Node cur = head;
		Node runner = cur;
		while (runner != null && runner.next != null) {
			if (runner.next.data < x) {
				Node temp = new Node(runner.next.data);
				temp.next = cur;
				cur = temp;
				runner.next = runner.next.next;
			}
			runner = runner.next;
		}
		return cur;
	}
}
