def find_element_by_class(driver, name, ignore_message=False):
    """Finds element by class name.

    Args:
        driver: WebDriver object.
        name: Class name.
        ignore_message: Boolean value indicating whether to ignore error message.

    Returns:
        Element object.
    """
    try:
        element = driver.find_element_by_class_name(name)
    except NoSuchElementException:
        if not ignore_message:
            raise WebDriverException(f'Cannot find element with class name: {name}')
        else:
            return None
    return element

