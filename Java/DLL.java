import java.util.Scanner;
class DLLNode{
    int data;
    DLLNode next;
    DLLNode prev;

    public void setData(int data){
        this.data=data;
    }
    public void setNext(DLLNode next){
        this.next=next;
    }
    public int getData(){
        return data;
    }
    public DLLNode getNext(){
        return next;
    }
    public void setPrev(DLLNode next){
        this.prev=prev;
    }
    public DLLNode getPrev(){
        return prev;
    }
}

 class DoublyLinkedList {
    private DLLNode head;
    int size = 0;

    DoublyLinkedList() {
        head = null;
    }

    public void Traverse() {
        DLLNode ptr = head;
        if (ptr == null) {
            System.out.println("The list is empty");
        } else {
            System.out.println("The list is :");
            while (ptr != null) {
                System.out.print(ptr.getData());
                System.out.print("  ");
                ptr = ptr.getNext();
            }
        }
    }

    public void insertatfront(int data) {
        DLLNode newnode=new DLLNode();
        newnode.setData(data);
        newnode.setNext(head);
        newnode.setPrev(null);
        head=newnode;
    }
    public void insertatend(int data) {
        DLLNode newnode=new DLLNode();
        if(head==null)
        {
            insertatfront(data);
        }
        else {
            DLLNode ptr=head;
            while(ptr.getNext()!=null) {
                ptr=ptr.getNext();

            }
            newnode.setData(data);
            newnode.setNext(null);
            newnode.setPrev(ptr);
            ptr.setNext(newnode);
        }
    }


     void deletefrontNode() {
         if (head == null) {
             System.out.println("The list is empty");
         } else {
             DLLNode temp = head;
             head = temp.getNext();
         }
     }
     public void insertat(int index,int data)
     {
         if((index<0)||(index>size))
             System.out.println("Insertion not possible");
         else if ((head==null) && (size==0))
             insertatfront(data);
         else
         {
             DLLNode newNode = new DLLNode();
             newNode.setData(data);
             DLLNode ptr=head;
             int i=0;
             while(i<index-1)
             {
                 i++;
                 ptr=ptr.getNext();
             }
             newNode.next=ptr.getNext();
             ptr.setNext(newNode);
         }
     }
}
public class DDL {
    public static void main(String[] args) {
        DoublyLinkedList dll1 = new DoublyLinkedList();
        Scanner sc= new Scanner(System.in);
        while (true){
            System.out.println(" \n");
            System.out.println("CHOICES");
            System.out.println("1.Traveseal");
            System.out.println("2.Insert a node at front");
            System.out.println("3.Insert a node at end");
            System.out.println("4.Insert a node at an index");
            System.out.println("5.Delete a node from front ");
            System.out.println("Enter you choice(enter Q for exit) : ");
            char ch = sc.next().charAt(0);
            int tkn=ch-'0';
            if(tkn==1){
                dll1.Traverse();
            }
            else if(tkn==2){
                System.out.println("Enter the data for new node : ");
                int data = sc.nextInt();
                dll1.insertatfront(data);
            }
            else if(tkn==3){
                System.out.println("Enter the data for new node : ");
                int data = sc.nextInt();
                dll1.insertatend(data);
            }
            else if(tkn==4){
                System.out.println("Enter the data for new node : ");
                int data = sc.nextInt();
                System.out.println("Enter the index : ");
                int indx = sc.nextInt();
                dll1.insertat(indx,data);
            }
            else if(tkn==5){
                dll1.deletefrontNode();
            }
            else if(ch=='Q'){
                break;
            }
        }

    }
}
