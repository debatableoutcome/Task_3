from selenium.webdriver.common.by import By


class ConstructorLocators:
    INGREDIENTS_LIST = (By.CSS_SELECTOR, '[class*="BurgerIngredients_ingredients__"]')
    INGREDIENT_CARD = (By.CSS_SELECTOR, '[class*="BurgerIngredient_ingredient__"]')
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, '[class*="counter_counter__"]')
    CONSTRUCTOR_DROPZONE = (By.XPATH, '//span[contains(text(), "Перетяните булочку сюда (верх)")]')
    BUNS_SECTION = (By.XPATH, "//h2[contains(text(),'Булки')]/following-sibling::ul")
    SAUCES_SECTION = (By.XPATH, "//h2[contains(text(),'Соусы')]/following-sibling::ul")
    FIRST_BUN_CARD = (By.XPATH, "//h2[contains(text(),'Булки')]/following::a[contains(@class,'BurgerIngredient_ingredient')][1]")
    FIRST_SAUCE_CARD = (By.XPATH, "//h2[contains(text(),'Соусы')]/following::a[contains(@class,'BurgerIngredient_ingredient')][1]")
    FILLINGS_SECTION = (By.XPATH, "//h2[contains(text(),'Начинки')]/following-sibling::ul")
    ORDER_BUTTON = (By.XPATH, '//button[contains(text(), "Оформить заказ")]')

    INGREDIENT_MODAL = (By.CSS_SELECTOR, '[class*="Modal_modal__contentBox__"]')
    INGREDIENT_MODAL_STATS = (By.CSS_SELECTOR, '[class*="Modal_modal__statsList__"]')
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, '[class*="Modal_modal__close_modified__"]')
    ORDER_SUCCESS_TEXT = (By.XPATH, '//p[contains(text(), "Ваш заказ начали готовить")]')



    
