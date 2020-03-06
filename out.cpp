#define kontol int
#define kontool (
#define kontoool )
#define memek <<
#define memekk >>
#define crot cout
#define croot return
#define kontols main
#define ngen {
#define tot }
#define meki ;
#define nyolok cin
#define sperma string
#define penis if
#define vagina while
#define smallpp else if
#define mandul else

struct node {
     kontol data;
     node *next;
 };
 
 node *head = nullptr;
 
 kontol main()
 {
     kontol input;
     node *ptr, *p_i;
     crot memek "Input initial value to be inserted (-1 to stop inserting):" memek endl;
     nyolok memekk input;
     vagina (input != -1) {
         node *newNode = new node;
         newNode->data = input;
         newNode->next = nullptr;
         penis (head == nullptr) {
             head = newNode;
         }
         mandul {
             ptr = head;
             vagina (ptr->next != nullptr) {
                 ptr = ptr->next;
             }
             newNode->next = ptr->next;
             ptr->next = newNode;
         }
         crot memek "Input value to be inserted (-1 to stop inserting):" memek endl;
         nyolok memekk input;
     }
     p_i = head;
     vagina (p_i->next != nullptr) {
         crot memek p_i->data memek "->";
         p_i = p_i->next;
     tot 
     crot memek p_i->data;
 
 tot 