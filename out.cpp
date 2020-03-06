#include<iostream>
#include<string>
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


using namespace std meki 

struct node ngen 
    kontol  data meki 
    node *next meki 
tot  meki 

node *head = nullptr meki 

kontol  kontols kontool kontoool 
ngen 
    kontol  input meki 
    node *ptr, *p_i meki 
    crot  memek  "Input initial value to be inserted (-1 to stop inserting):"  memek  endl meki 
    nyolok  memekk  input meki 
    vagina  kontool input != -1) ngen 
        node *newNode = new node meki 
        newNode->data = input meki 
        newNode->next = nullptr meki 
        penis  kontool head == nullptr) ngen 
            head = newNode meki 
        tot 
        mandul  ngen 
            ptr = head meki 
            vagina  kontool ptr->next != nullptr) ngen 
                ptr = ptr->next meki 
            tot 
            newNode->next = ptr->next meki 
            ptr->next = newNode meki 
        tot 
        crot  memek  "Input value to be inserted (-1 to stop inserting):"  memek  endl meki 
        nyolok  memekk  input meki 
    tot 
    p_i = head meki 
    vagina  kontool p_i->next != nullptr) ngen 
        crot  memek  p_i->data memek  "->"  meki 
        p_i = p_i->next meki 
    tot  
    crot  memek  p_i->data meki 

tot