import java.util.Scanner;

class Node{
    int data;
    Node next;

    public void setData(int data){
        this.data=data;
    }
    public void setNext(Node next){
        this.next=next;
    }
    public int getData(){
        return data;
    }
    public Node getNext(){
        return next;
    }
}

class SinglyLinkedList {
    private Node head;
    int size=0;
    SinglyLinkedList(){
        head=null;
    }
    public void Traverse(){
        Node ptr = head;
        if (ptr==null){
            System.out.println("The list is empty");
        }else{
            System.out.println("The list is :");
            while (ptr!=null){
                System.out.print(ptr.getData());
                System.out.print("  ");
                ptr=ptr.getNext();
            }
        }

    }
    public void insertFront(Node node){
        if(head==null){
            head=node;
        }
        else{
            Node temp=head;
            head=node;
            node.setNext(temp);
        }
    }

    public void insertAt(int index, int data){
        Node new_node = new Node();
        new_node.setData(data);
        new_node.setNext(null);

        if(index < 1 || index > size + 1)
            System.out.println("Invalid\n");
        else if(index == 1){
            new_node.next = head;
            head = new_node;
            size++;
        }

        else
        {
            Node temp = head;

            while(--index > 1){
                temp = temp.next;
            }
            new_node.next= temp.next;
            temp.next = new_node;
            size++;
        }
    }

    public void deleteFront(){
        if(head==null){
            System.out.println("The list is empty");
        }
        else{
            Node temp=head;
            head=temp.getNext();

        }
    }

    public void deleteAll(int data){
        if(head==null){
            System.out.println("The list is empty");
        }
        else{
            Node temp = head, prev = null;
            while (temp != null && temp.data == data)
            {
                head = temp.next;
                temp = head;
            }

            while (temp != null)
            {
                while (temp != null && temp.data != data)
                {
                    prev = temp;
                    temp = temp.next;
                }
                if (temp == null)
                    return;
                prev.next = temp.next;
                temp = prev.next;
            }

        }
    }

    public int frequency(int data){
        Node ptr = head;
        int cnt=0;
        if (ptr==null){
            System.out.println("The list is empty");
            return 0;
        }else {
            while (ptr != null) {
                if (ptr.getData() == data) {
                    cnt += 1;
                }
                ptr = ptr.getNext();
            }
        }
        return cnt;
    }

    public void insertEnd(Node node){
        if(head==null){
            head=node;
        }
        else{
            Node ptr = head;
            Node prev = new Node();
                while (ptr!=null){
                    prev=ptr;
                    ptr=ptr.getNext();
                }
                prev.setNext(node);

        }
    }


    public void Search(int data){
        Node ptr = head;
        if (ptr==null){
            System.out.println("The list is empty");
        }else{
            while (ptr!=null){
                if(ptr.getData()==data){
                    System.out.println("Element found");
                    break;
                }
                ptr=ptr.getNext();
            }
        }

    }

    public int getSize(){
        Node ptr = head;
        if (ptr==null){
            System.out.println("The list is empty");
            return 0;
        }else{
            while (ptr!=null){
                size=size+1;
                ptr=ptr.getNext();
            }
        }
        return size;
    }

}

public class SinglyLinkedListD {
    public static void main(String[] args) {
        SinglyLinkedList sl1 = new SinglyLinkedList();
        Scanner sc= new Scanner(System.in);
        while (true){
            System.out.println(" \n");
            System.out.println("CHOICES");
            System.out.println("1.Traveseal");
            System.out.println("2.Insert a node at front");
            System.out.println("3.Insert a node at end");
            System.out.println("4.Delete a node at front");
            System.out.println("5.Search for an element");
            System.out.println("6.Get the size");
            System.out.println("7.Insert element at a specific index");
            System.out.println("8.Delete the first occurance of the data from the list.");
            System.out.println("9.Get frequency of an element");
            System.out.println("Enter you choice(enter Q for exit) : ");
            char ch = sc.next().charAt(0);
            int tkn=ch-'0';
            if(tkn==1){
                sl1.Traverse();
            }
            else if(tkn==2){
                Node node1 = new Node();
                System.out.println("Enter the data for new node : ");
                int data = sc.nextInt();
                node1.setData(data);
                sl1.insertFront(node1);
            }
            else if(tkn==3){
                Node node1 = new Node();
                System.out.println("Enter the data for new node : ");
                int data = sc.nextInt();
                node1.setData(data);
                sl1.insertEnd(node1);
            }
            else if(tkn==4){
                sl1.deleteFront();
            }
            else if(tkn==5){
                System.out.println("Enter the data to be searched for : ");
                int data = sc.nextInt();
                sl1.Search(data);
            }
            else if(tkn==6){
                System.out.println("The size of the list is : "+ sl1.getSize());
            }
            else if(tkn==7){
                System.out.println("Enter the data for new node : ");
                int data = sc.nextInt();
                System.out.println("Enter the index : ");
                int indx = sc.nextInt();
                sl1.insertAt(indx,data);
            }
            else if(tkn==8){
                System.out.println("Enter the element for deletion : ");
                int n = sc.nextInt();
                sl1.deleteAll(n);
            }

            else if(tkn==9){
                System.out.println("Enter the element : ");
                int n = sc.nextInt();
                sl1.frequency(n);
            }
            else if(ch=='Q'){
                break;
            }
        }

    }
}
