struct node {
    int data;
    node *next;
};

node *head = nullptr;

int main()
{
    int input;
    node *ptr, *p_i;
    cout << "Input initial value to be inserted (-1 to stop inserting):" << endl;
    cin >> input;
    while (input != -1) {
        node *newNode = new node;
        newNode->data = input;
        newNode->next = nullptr;
        if (head == nullptr) {
            head = newNode;
        }
        else {
            ptr = head;
            while (ptr->next != nullptr) {
                ptr = ptr->next;
            }
            newNode->next = ptr->next;
            ptr->next = newNode;
        }
        cout << "Input value to be inserted (-1 to stop inserting):" << endl;
        cin >> input;
    }
    p_i = head;
    while (p_i->next != nullptr) {
        cout << p_i->data << "->";
        p_i = p_i->next;
    } 
    cout << p_i->data;

}