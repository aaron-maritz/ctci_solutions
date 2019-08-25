package chapter_2;  //  For Node Class

//  Write code to remove duplicates from an unsorted linked list
//  Two ways to go about it, take everything, insert into a hashmap -> return new list
//  Or -> Just run through it if you're not allowed temporary storage
public class QuestionOne {

	public static void main(String[] args) {
		//  Node n = new Node(5);
		Node list = new Node(5);
		list.next = new Node(5);
		list.next.next = new Node(5);
		list.next.next.next = new Node(6);
		Node list2 = new Node(4);
		list = removeDups(list);
		list2 = removeDups(list2);
		System.out.println(list.data);
		System.out.println(list.next.data);
	}
	
	//  Get O(N^2) here, where N is the # of nodes -> Runs through each node, and each node has to check every other remaining node in the list
	//  Reference Semantics are being annoying, you know how the algorithm works it's fine
	public static Node removeDups(Node head) {
		if (head != null) {
			Node temp = head;
			while (temp.next != null) {
				Node runner = temp.next;
				Node prior = temp;
				while (runner != null) {
					if (runner.data == head.data) {
						//  Remove runner
						System.out.println("removing :" + runner.data);
						prior.next = runner.next;
					}
					prior = prior.next;
					runner = runner.next;
				}
				temp = temp.next;
			}
		}
		return head;
	}
}
