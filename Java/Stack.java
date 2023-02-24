//Stack using Array
import java.util.*;

public class Stack {
    int top;
    int size;
    int[] arr;

    Stack(int size) {
        this.size = size;
        arr = new int[size];
        top = -1;
    }

    public void push(int data) {
        if (top == size - 1) {
            System.out.println("Stack is full");
        } else {
            top++;
            arr[top] = data;
        }
    }

    public int pop() {
        if (top == -1) {
            System.out.println("Stack is empty");
            return -1;
        } else {
            int data = arr[top];
            top--;
            return data;
        }
    }

    public int peek() {
        if (top == -1) {
            System.out.println("Stack is empty");
            return -1;
        } else {
            return arr[top];
        }
    }

    public void display() {
        if (top == -1) {
            System.out.println("Stack is empty");
        } else {
            for (int i = top; i >= 0; i--) {
                System.out.println(arr[i]);
            }
        }
    }

    public static void main(String[] args) {
        Stack s = new Stack(5);
        s.push(10);
        s.push(20);
        s.push(30);
        s.push(40);
        s.push(50);
        s.push(60);
        s.display();
        System.out.println("Peek element is " + s.peek());
        System.out.println("Pop element is " + s.pop());
        System.out.println("Peek element is " + s.peek());
        s.display();
    }
}
