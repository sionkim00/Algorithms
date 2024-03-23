            A_next = A.next
            B_next = B.next

            A.next = B
            B.next = A_next

            A = A_next
            B = B_next
[
