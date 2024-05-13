'''
    Test Ticket class
    Hang Zhao
    11/16/2023
'''
import unittest
from Queue import Queue
from Tickets import Tickets


class TestTickets(unittest.TestCase):
    ''' Test class for Tickets'''

    def test_serve_customer(self):
        ''' test serve_customer'''
        q = Queue(3)
        q.enqueue(1)
        ticket = Tickets()
        ticket.serve_customer(q)
        self.assertEqual(q.size(), 0)

    def test_simulate_ticket_line(self):
        ''' test simulate_ticket_line'''
        ticket = Tickets()
        ticket.simulate_ticket_line(0)
        ticket.simulate_ticket_line(1)


if __name__ == "__main__":
    unittest.main()
