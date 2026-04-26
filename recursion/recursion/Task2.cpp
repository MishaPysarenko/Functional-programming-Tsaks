struct Node {
    int val;
    Node* next;
    Node(int v) : val(v), next(nullptr) {}
};

/* =======================
   ÇÂÈ×ÀÉÍÀ ÐÅÊÓÐÑ²ß
   ======================= */
Node* swapPairsRec(Node* head) {
    if (!head || !head->next) return head;

    Node* first = head;
    Node* second = head->next;

    first->next = swapPairsRec(second->next);
    second->next = first;

    return second;
}

/* =======================
   ÕÂÎÑÒÎÂÀ ÐÅÊÓÐÑ²ß
   ======================= */
Node* swapPairsTail(Node* prev, Node* curr, Node* head) {
    if (!curr || !curr->next) {
        if (prev) prev->next = curr;
        return head;
    }

    Node* first = curr;
    Node* second = curr->next;
    Node* nextPair = second->next;

    second->next = first;

    if (prev) prev->next = second;
    else head = second;

    first->next = nextPair;

    return swapPairsTail(first, nextPair, head);
}

Node* swapPairsTailWrapper(Node* head) {
    return swapPairsTail(nullptr, head, head);
}