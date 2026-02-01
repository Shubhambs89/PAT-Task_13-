from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from time import sleep

class TestDragDrop:
    #Browsing method
    @pytest.fixture(autouse=True)    
    def setup(self):
        self.url = "https://jqueryui.com/droppable/"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

        #mouse action chains
        self.driver.get(self.url)
        
        # Locators for draggable and target object
        self.source_1 = 'draggable'
        self.target_1 = 'droppable'

        yield
        self.driver.quit()


    #ActionChanins drag and drop
    def test_positive_drag_drop(self):
        self.driver.switch_to.frame(0)
        source_1_webelement = self.driver.find_element(by=By.ID, value=self.source_1)
        target_1_webelement = self.driver.find_element(by=By.ID, value=self.target_1)

        action = ActionChains(self.driver)
        action.drag_and_drop(source_1_webelement, target_1_webelement).perform()
        

        assert target_1_webelement.text == "Dropped!"

    def test_negative_drag_and_drop_offset(self):
        self.driver.switch_to.frame(0)
        
        source = self.driver.find_element(By.ID, "draggable")
        target = self.driver.find_element(By.ID, "droppable")
        
        actions = ActionChains(self.driver)
     
        actions.drag_and_drop_by_offset(source, 20, 20).perform()

        assert target.text == "Drop here"