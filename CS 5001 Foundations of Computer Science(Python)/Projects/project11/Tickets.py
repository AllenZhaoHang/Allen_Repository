'''
    Ticket class
    Hang Zhao
    11/16/2023
'''
import random
from Queue import Queue


class Tickets:
    ''' Tickets class'''

    def serve_customer(self, queue):
        ''' serve_customer -- serves the next customer in the queue'''
        if not queue.is_empty():
            customer = queue.dequeue()
            print(f"Serving customer {customer}")

    def simulate_ticket_line(self, num_iterations):
        ''' simulate_ticket_line -- simulates a ticket line for a given number of iterations'''
        queue = Queue(100)
        num_entered_queue = 0
        ticket = Tickets()
        for i in range(num_iterations):
            num_customers = random.randint(0, 2)
            for j in range(num_customers):
                if not queue.is_full():
                    queue.enqueue(num_entered_queue)
                    num_entered_queue += 1
            ticket.serve_customer(queue)

        print(f"{queue.size()} people still in the queue")


if __name__ == "__main__":
    ticket = Tickets()
    ticket.simulate_ticket_line(100)
