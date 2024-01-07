import java.util.Arrays;

public class Medium_AddTwoNumbers {

	public static void main(String[] args){
		addTwoNumbers(createList(9,9,9,9,9,9,9), createList(9,9,9,9));
	}

	private static ListNode createList(int...nums){
		if (nums == null || nums.length == 0)
			return new ListNode();
		ListNode result = new ListNode(nums[0]);
		ListNode previousNode = result;
		for (int i = 1; i < nums.length; i++) {
			int num = nums[i];
			ListNode node = new ListNode(num);
			previousNode.next = node;
			previousNode = node;
		}
		return result;
	}

	public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		ListNode result = null;
		int resto = 0;
		ListNode previousNode = new ListNode();
		do {
			int num = l1.val + l2.val + resto;
			if (num >= 10){
				resto = num / 10;
				num = num % 10;
			} else {
				resto = 0;
			}
			ListNode node = new ListNode(num);
			if (result == null)
				result = node;
			else
				previousNode.next = node;
			previousNode = node;
			l1 = l1.next;
			l2 = l2.next;
		} while (l1 != null && l2 != null);

		ListNode remaining = l1 == null ? l2 : l1;
		if (remaining != null) {
			previousNode.next = remaining;
			do {
				remaining.val += resto;
				if(remaining.val == 10) {
					resto = 1;
					remaining.val = 0;
				} else {
					resto = 0;
				}
				previousNode = remaining;
			} while ((remaining = remaining.next) != null && resto > 0);
		}
		if (resto == 1) {
			previousNode.next = new ListNode(1);
		}
		return result;
	}

	private static class ListNode {
		int val;
		ListNode next;

		ListNode() {
		}

		ListNode(int val) {
			this.val = val;
		}

		ListNode(int val, ListNode next) {
			this.val = val;
			this.next = next;
		}
	}
}
