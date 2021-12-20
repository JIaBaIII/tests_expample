from framework.TociPages import FindHelper, ClickHelper, WriteHelper, MakeHelper


class Chrome(FindHelper, ClickHelper, WriteHelper, MakeHelper):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        driver.set_window_size(937, 1000)
        driver.set_window_position(7, 10)
        driver.implicitly_wait(0.5)


class FireFox(FindHelper, ClickHelper, WriteHelper, MakeHelper):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        driver.set_window_size(850, 1000)
        driver.set_window_position(934, 10)
        driver.implicitly_wait(0.5)
