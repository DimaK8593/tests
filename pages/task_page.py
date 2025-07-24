from playwright.sync_api import Page

class TaskPage:

    def __init__(self, page: Page):
        self.page = page
        self.add_task_button = page.locator("[class='fc42413d _27c1200b _297575f4 c4a9b3ab c5d6948b']")
        self.task_input = page.locator("[aria-label='Task name']")
        self.submit_button = page.locator("[data-testid='task-editor-submit-button']")
        self.task_items = page.locator(".task_list_item__content")

    def add_task(self, text: str):
        self.add_task_button.click()
        self.task_input.click()
        self.task_input.type(text) 
        self.submit_button.click()

    def is_task_present(self, text: str) -> bool:
        locator = self.page.locator(f"//div[contains(text(), '{text}')]")
        try:
            locator.wait_for(state="visible")
            return True
        except TimeoutError:
            return False