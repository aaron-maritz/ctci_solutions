package chapter_2;


//  Author: Aaron Maritz
//	Implement an Algorithm to find the kth to last element of a singly linked list
//	Thoughts:	N total elements -> want to find find element N - k
//	Initial thought -> Just Get Two Pointers -> Have one go k elements up, then have them both go one by one till first pointer
//	Hits the end of the linked list.
public class QuestionTwo {

	//  Notice I'm assuming that k is positive, and head is a non-null linked list, with n elements such that n > k.
	//	Could check for this later -> But probably unneccessary at the moment.
	public int findKthToEnd(Node head, int k) {
		Node cur = head;
		Node runner = head;
		while (k > 0) {
			runner = runner.next;
			k--;
		}
		while (runner != null) {
			runner = runner.next;
			cur = cur.next;
		}
		return cur.data;
	}
	//  Email check
}
