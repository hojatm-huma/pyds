class DequeTestMixin:
    def test_addfirst_removefirst(self):
        deque = self.DequeCls()

        FINAL_RESULT = list(range(0, 10))

        for i in reversed(FINAL_RESULT):
            deque.addfirst(i)

        self.assertEqual(deque.len(), len(FINAL_RESULT))

        for i in FINAL_RESULT:
            self.assertEqual(deque.removefirst(), i)

    def test_addfirst_removelast(self):
        deque = self.DequeCls()

        FINAL_RESULT = list(range(0, 10))

        for i in reversed(FINAL_RESULT):
            deque.addfirst(i)

        self.assertEqual(deque.len(), len(FINAL_RESULT))

        for i in reversed(FINAL_RESULT):
            self.assertEqual(deque.removelast(), i)

    def test_addlast_removefirst(self):
        deque = self.DequeCls()

        FINAL_RESULT = list(range(0, 10))

        for i in FINAL_RESULT:
            deque.addlast(i)

        self.assertEqual(deque.len(), len(FINAL_RESULT))

        for i in FINAL_RESULT:
            self.assertEqual(deque.removefirst(), i)

    def test_addlast_removelast(self):
        deque = self.DequeCls()

        FINAL_RESULT = list(range(0, 10))

        for i in FINAL_RESULT:
            deque.addlast(i)

        self.assertEqual(deque.len(), len(FINAL_RESULT))

        for i in reversed(FINAL_RESULT):
            self.assertEqual(deque.removelast(), i)
