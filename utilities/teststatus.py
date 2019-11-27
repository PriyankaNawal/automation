from base.selenium_driver import SeleniumDriver
import logging
import utilities.custom_logger as cl


class TestStatus(SeleniumDriver):
    log=cl.custom_logger(logging.INFO)

    def __init__(self,driver):
        super(TestStatus,self).__init__(driver)
        self.result_list=[]

    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.result_list.append("PASS")
                    self.log.info("####VERIFICATION SUCCESSFUL :: " + result_message)
                else:
                    self.result_list.append("FAIL")
                    self.log.error("####VERIFICATION FAILED :: " + result_message)
                    self.screenshot(result_message)
            else:
                self.result_list.append("FAIL")
                self.log.error("####VERIFICATION FAILED :: " + result_message)
                self.screenshot(result_message)
        except:
            self.result_list.append("FAIL")
            self.log.error("#### Exception occurred!!")
            self.screenshot(result_message)

    def mark(self, result, result_message):
        self.set_result(result, result_message)

    def mark_final(self, testname, result, result_message):
        self.set_result(result, result_message)
        if "FAIL" in self.result_list:
            self.log.error(testname + " #### TEST FAILED")
            self.result_list.clear()
            assert True == False
        else:
            self.log.info(testname + " #### TEST SUCCESSFUL")
            self.result_list.clear()
            assert True==True
