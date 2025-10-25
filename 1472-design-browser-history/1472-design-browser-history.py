class BrowserHistory:

    def __init__(self, homepage: str):
        self.browser_history = [homepage]
        self.curr_index = 0
        
    def visit(self, url: str) -> None:
        self.browser_history = self.browser_history[: self.curr_index + 1]
        self.browser_history.append(url)
        self.curr_index = len(self.browser_history) - 1

    def back(self, steps: int) -> str:
        if steps > self.curr_index:
            self.curr_index = 0
        else:
            self.curr_index -= steps
        return self.browser_history[self.curr_index]

    def forward(self, steps: int) -> str:
        if self.curr_index + steps >= len(self.browser_history):
            self.curr_index = len(self.browser_history) - 1
        else:
            self.curr_index += steps
        
        return self.browser_history[self.curr_index]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)